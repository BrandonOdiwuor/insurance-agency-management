from flask import Blueprint, request, render_template, \
                  flash, g, session, redirect, url_for

from app.controller import verify_user, verify_customer

from app.forms import LoginForm

mod_app = Blueprint('app', __name__, url_prefix='/')

@mod_app.route('/signin/', methods=['GET', 'POST'])
def signin():

    form = LoginForm(request.form)

    if form.validate_on_submit():

        user = verify_user(form.email.data, form.password.data)

        if user:

            session['user'] = user.id

            flash('Welcome %s' % user.name)

            return redirect(url_for('auth.home'))

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

            return redirect(url_for('auth.home'))

        flash('Wrong email or password', 'error-message')

    return render_template("signin.html", form=form)

# @mod_app.route('/signin/', methods=['GET', 'POST'])
# def signin():