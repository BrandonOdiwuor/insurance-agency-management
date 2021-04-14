from os import environ
from flask import request, flash, redirect, render_template, \
    url_for, session
from . import auth
from .forms import LoginForm, CustomerRegistrationForm
from app.controllers import create_customer, verify_user, \
    verify_customer, create_user
from app.utils.utils import login_required, save_file
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
        attachment_id_front = save_file(form.attachment_id_front.data)
        attachment_id_back = save_file(form.attachment_id_back.data)
        customer_payload = {
            'first_name': form.first_name.data,
            'last_name': form.last_name.data,
            'national_id_number': form.national_id_number.data,
            'primary_phone_number': form.primary_phone_number.data,
            'primary_email': form.primary_email.data,
            'password': 'pass@123',  # To DO: -FIX autogenerate password
            'physical_address': form.physical_address.data,
            'city': form.city.data,
            'county': form.county.data,
            'postal_address': form.postal_address.data,
            'postal_code': form.postal_code.data,
            'gender': form.gender.data,
            'birth_date': form.birth_date.data,
            'kra_pin': form.kra_pin.data,
            'attachment_id_front': attachment_id_front,
            'attachment_id_back': attachment_id_back
        }
        create_customer(customer_payload)
        return redirect(url_for('admin.customers'))
    return render_template("auth/register-customer.html", form=form)


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
