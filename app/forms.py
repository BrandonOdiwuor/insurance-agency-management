from flask_wtf import FlaskForm # , RecaptchaField

from wtforms import SubmitField, TextField, PasswordField, StringField, validators

from wtforms.validators import Required, Email, EqualTo

class LoginForm(FlaskForm):
    email = StringField('Email Address', [
        validators.DataRequired(), 
        validators.Email(), 
        validators.Length(min=6, max=35)])
    password = PasswordField('Password', [validators.DataRequired()])

class NewCustomerForm(FlaskForm):
    first_name = StringField('First Name', [
        validators.DataRequired()])
    last_name = StringField('Last Name', [
        validators.DataRequired()])
    email = StringField('Email Address', [
        validators.DataRequired(), 
        validators.Email(), 
        validators.Length(min=6, max=35)])
    mobile_phone = StringField('Telephone', [
        validators.DataRequired(), 
        validators.Length(min=9, max=9)])
    id_no = StringField('ID Number', [
        validators.DataRequired(), 
        validators.Length(min=8, max=8)])