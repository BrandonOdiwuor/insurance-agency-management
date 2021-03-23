from flask import flash, redirect, render_template, url_for, session
from . import auth
from .forms import LoginForm, CustomerRegistrationForm
from app.controllers import create_customer, verify_user, verify_customer
from utils.utils import login_required


@auth.route('/register-customer', methods=['GET', 'POST'])
@login_required
def register_customer():
    """
    Handle requests to the /register-customer route
    Add a customer to the database through the registration form
    """
    form = CustomerRegistrationForm()

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
        return redirect(url_for('admin.customers'))
    return render_template("forms/customer.html", form=form)


@auth.route('/login', methods=['GET', 'POST'])
def login():
    """
    Handle requests to the /login route
    Log an employee in through the login form
    """
    form = LoginForm()

    if form.validate_on_submit():

        user = verify_user(form.email.data, form.password.data)

        if user:
            session['authorization'] = 'Bearer %s' % user.token()

            return redirect(url_for('admin.dashboard'))

        flash('Wrong email or password', 'error-message')

    return render_template("forms/signin.html", form=form)


@auth.route('/customer-login', methods=['GET', 'POST'])
def customer_signin():

    form = LoginForm()

    if form.validate_on_submit():

        customer = verify_customer(form.email.data, form.password.data)

        if customer:

            session['authorization'] = 'Bearer %s' % customer.token()

            return redirect(url_for('app.home'))

        flash('Wrong email or password', 'error-message')

    return render_template("forms/signin.html", form=form)


@auth.route('/logout')
@login_required
def logout():
    """
    Handle requests to the /logout route
    Log a user out through the logout link
    """
    session.clear()

    # redirect to the login page
    return redirect(url_for('home.homepage'))
