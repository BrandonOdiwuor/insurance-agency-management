import functools
from flask import Blueprint, request, render_template, \
    flash, g, session, redirect, url_for
from app.forms import LoginForm, NewCustomerForm, SaleItemForm
from app.controllers import verify_user, verify_customer, create_customer, \
    get_customers, update_customer_status, get_items_of_sale, create_item_of_sale
from utils.utils import decode_token

mod_app = Blueprint('app', __name__, url_prefix='/')


def login_required(view):
    @functools.wraps(view)
    def wrapped_view(**kwargs):
        if 'authorization' not in session:
            return redirect(url_for('app.signin'))

        return view(**kwargs)

    return wrapped_view


@mod_app.route('/signin/', methods=['GET', 'POST'])
def signin():

    form = LoginForm(request.form)

    if form.validate_on_submit():

        user = verify_user(form.email.data, form.password.data)

        if user:
            session['authorization'] = 'Bearer %s' % user.token()

            flash('Welcome {0} {1}'.format(user.f_name, user.l_name))

            return redirect(url_for('app.admin_home'))

        flash('Wrong email or password', 'error-message')

    return render_template("forms/signin.html", form=form)


@mod_app.route('customer/signin/', methods=['GET', 'POST'])
def customer_signin():

    form = LoginForm(request.form)

    if form.validate_on_submit():

        customer = verify_customer(form.email.data, form.password.data)

        if customer:

            session['customer'] = customer.id

            flash('Welcome %s' % customer.f_name)

            return redirect(url_for('app.home'))

        flash('Wrong email or password', 'error-message')

    return render_template("forms/signin.html", form=form)


@mod_app.route('/signout')
def logout():
    session.clear()
    return redirect(url_for('app.home'))


@mod_app.route('/', methods=['GET'])
def home():
    return render_template("home.html")


@mod_app.route('/admin/', methods=['GET'])
@login_required
def admin_home():
    print("path", request.path)
    return render_template("admin.html")


@mod_app.route('/customers/', methods=['GET'])
@login_required
def customers():
    customers = get_customers()
    return render_template("customers.html", customers=customers)


@mod_app.route('/new-customer/', methods=['GET', 'POST'])
@login_required
def new_customer():
    form = NewCustomerForm(request.form)

    if form.validate_on_submit():
        customer_payload = {
            'first_name': form.first_name.data,
            'last_name': form.last_name.data,
            'id_no': form.id_no.data,
            'phone': form.mobile_phone.data,
            'email': form.email.data,
            'password': 'pass@123'
        }
        create_customer(customer_payload)
        return redirect(url_for('app.customers'))
    return render_template("forms/customer.html", form=form)


@mod_app.route('/update-customer-status/<int:customer_id>', methods=['GET'])
@login_required
def v_update_customer_status(customer_id):
    update_customer_status(customer_id)
    return redirect(url_for('app.customers'))

@mod_app.route('/products/', methods=['GET'])
@login_required
def products():
    products = get_items_of_sale()
    return render_template("products.html", products=products)

@mod_app.route('/new-product/', methods=['GET', 'POST'])
@login_required
def new_product():
    form = SaleItemForm(request.form)

    if form.validate_on_submit():
        sale_item_payload = {
            'name': form.name.data,
            'category': form.category.data,
            'price': form.price.data
        }
        create_item_of_sale(sale_item_payload)
        return redirect(url_for('app.products'))
    return render_template("forms/product.html", form=form)