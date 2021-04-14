from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileRequired
from wtforms import PasswordField, StringField, SelectField, \
    SubmitField, ValidationError, validators
from ..controllers import validate_customer_email, validate_customer_telephone
from wtforms.fields.html5 import EmailField, TelField, IntegerField, DateField


class CustomerRegistrationForm(FlaskForm):
    """
    Form by admin user to create new customer account
    """
    first_name = StringField('First Name', [validators.InputRequired()])
    last_name = StringField('Last Name', [validators.InputRequired()])
    primary_email = EmailField('Email Address', [
        validators.InputRequired(), validators.Email()
    ])
    primary_phone_number = TelField('Telephone', [
        validators.InputRequired(), validators.Length(min=9, max=9)
    ])
    national_id_number = StringField('National ID Number', [
        validators.InputRequired(), validators.Length(min=8, max=8)
    ])
    physical_address = StringField('Physical Adress', [validators.InputRequired()])
    city = StringField('City', [validators.InputRequired()])
    county = StringField('County', [validators.InputRequired()])
    postal_address = StringField('Postal Adress', [validators.InputRequired()])
    postal_code = StringField('Postal Code', [validators.InputRequired()])
    gender = SelectField('Gender', [validators.InputRequired()])
    birth_date = DateField('Date Of Birth', [validators.InputRequired()])
    kra_pin = StringField('KRA Pin', [validators.InputRequired()])
    attachment_id_front = FileField('ID Front', validators=[FileRequired()])
    attachment_id_back = FileField('ID Back', validators=[FileRequired()])

    def validate_primary_email(self, field):
        if validate_customer_email(field.data):
            raise ValidationError('Email is already in use.')

    def validate_primary_phone_number(self, field):
        if validate_customer_telephone(field.data):
            raise ValidationError('Mobile phone is already in registered.')


class LoginForm(FlaskForm):
    """
    Form for users to login
    """
    email = EmailField('Email Address', [
        validators.InputRequired(),
        validators.Email()])
    password = PasswordField('Password', [validators.InputRequired()])
    submit = SubmitField('Sign in')
