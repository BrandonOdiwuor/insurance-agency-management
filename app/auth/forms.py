from flask_wtf import FlaskForm
from wtforms import PasswordField, StringField, SubmitField, ValidationError, validators
from ..controllers import validate_customer_email, validate_customer_telephone


class CustomerRegistrationForm(FlaskForm):
    """
    Form for to crethe admin to create new customer account
    """
    first_name = StringField('First Name', [
        validators.InputRequired()])
    last_name = StringField('Last Name', [
        validators.InputRequired()])
    email = StringField('Email Address', [
        validators.InputRequired(),
        validators.Email(),
        validators.Length(min=6, max=35)])
    mobile_phone = StringField('Telephone', [
        validators.InputRequired(),
        validators.Length(min=9, max=9)])
    id_no = StringField('ID Number', [
        validators.InputRequired(),
        validators.Length(min=8, max=8)])

    def validate_email(self, field):
        if validate_customer_email(field.data):
            raise ValidationError('Email is already in use.')

    def validate_mobile_phone(self, field):
        if validate_customer_telephone(field.data):
            raise ValidationError('Mobile phone is already in registered.')


class LoginForm(FlaskForm):
    """
    Form for users to login
    """
    email = StringField('Email Address', [
        validators.InputRequired(),
        validators.Email(),
        validators.Length(min=6, max=35)])
    password = PasswordField('Password', [validators.InputRequired()])
    submit = SubmitField('Sign in')
