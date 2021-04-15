from os import environ
from flask import request, flash, redirect, render_template, \
    url_for, session
from . import auth
from .forms import LoginForm, CustomerRegistrationForm, CustomerUpdateForm
from app.controllers import create_customer, verify_user, \
    verify_customer, create_user, get_customer, edit_customer
from app.utils.utils import login_required, save_file, get_customer_form_payload
from app.utils.enums import GenderChoices


@auth.route("/create-admin", methods=['POST'])
def create_admin():
    data = request.get_json()
    if data['DEV_KEY'] == environ.get("DEV_KEY"):
        user_payload = dict(
            first_name=data['first_name'],
            last_name=data['last_name'],
            email=data['email'],
            password=data['password'],
            phone=data['phone']
        )
        create_user(user_payload)
        return 'ok'
    else:
        return "security error!"


@auth.route('/register-customer', methods=['GET', 'POST'])
@login_required
def register_customer():
    form = CustomerRegistrationForm()
    form.gender.choices = [
        (gender_choice.name, gender_choice.name) for gender_choice in GenderChoices
    ]

    if form.validate_on_submit():
        customer_payload = get_customer_form_payload(form)
        customer_payload['attachment_id_front'] = save_file(
            form.attachment_id_front.data
        )
        customer_payload['attachment_id_back'] = save_file(
            form.attachment_id_back.data
        )
        create_customer(customer_payload)
        return redirect(url_for('admin.customers'))
    return render_template("auth/register-customer.html", form=form, form_to="/register-customer")


@auth.route('/update-customer/<string:customer_id>', methods=['GET', 'POST'])
@login_required
def update_customer(customer_id):
    customer = get_customer(customer_id)
    form = CustomerUpdateForm(obj=customer)
    form.gender.choices = [
        (gender_choice.name, gender_choice.name) for gender_choice in GenderChoices
    ]
    if form.validate_on_submit():
        edit_customer(customer_id, get_customer_form_payload(form))
        return redirect(url_for('admin.customer', customer_id=customer_id))
    return render_template("auth/update-customer.html", form=form, form_to="/update-customer/%s" % customer_id)


@auth.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()

    if form.validate_on_submit():
        user = verify_user(form.email.data, form.password.data)

        if user:
            session['authorization'] = 'Bearer %s' % user.token()
            return redirect(url_for('admin.dashboard'))
        else:
            form.email.errors.append('Wrong email or password')

    return render_template("auth/signin.html", form=form, action="/login")


@auth.route('/customer-login', methods=['GET', 'POST'])
def customer_signin():
    form = LoginForm()

    if form.validate_on_submit():
        customer = verify_customer(form.email.data, form.password.data)

        if customer:
            session['authorization'] = 'Bearer %s' % customer.token()
            return redirect(url_for('app.home'))
        else:
            form.email.errors.append('Wrong email or password')

    return render_template("auth/signin.html", form=form, action="/customer-login")


@auth.route('/logout')
@login_required
def logout():
    session.clear()

    # redirect to the login page
    return redirect(url_for('home.homepage'))
