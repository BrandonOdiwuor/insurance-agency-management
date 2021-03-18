import functools
from flask import Blueprint, request, render_template, \
                  flash, g, session, redirect, url_for
from app.forms import LoginForm, NewCustomerForm
from app.controller import verify_user, create_customer, get_customers
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

    return render_template("signin.html", form=form)

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

    return render_template("signin.html", form=form)

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
    return render_template("admin_home.html")

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
        customer = create_customer(customer_payload)
        return redirect(url_for('app.customers'))
    return render_template("new_customer.html", form=form)