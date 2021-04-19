from flask_wtf import FlaskForm
from wtforms import StringField, SelectField, IntegerField, \
    HiddenField, validators, BooleanField
from wtforms.fields.html5 import DateTimeLocalField, DecimalField, DateField


class SaleItemForm(FlaskForm):
    name = StringField('Product Name', [
        validators.InputRequired()])
    category = StringField('Product Category', [
        validators.InputRequired()
    ])
    price = DecimalField('Price', [validators.InputRequired()])


class CustomerInvoiceForm(FlaskForm):
    due_at = DateTimeLocalField('Invoice Due-Date', [
        validators.InputRequired()])
    price = DecimalField('Price', [validators.InputRequired()])
    item = SelectField(
        'Product',
        [validators.InputRequired()],
        coerce=int
    )


class CustomerInvoicePaymentForm(FlaskForm):
    invoice_id = HiddenField('invoice_id', [validators.InputRequired()])
    amount = DecimalField('Amount(Ksh.)', [validators.InputRequired()])
    payment_mode = SelectField('Payment Mode')


class BaseProductForm(FlaskForm):
    product_type = HiddenField(
        'Product Type', [validators.InputRequired()]
    )
    policy_start_date = DateField(
        'When do you want your cover to start?',
        [validators.InputRequired()]
    )
    sum_insured = DecimalField(
        'Insurable Amount(Ksh.)', [validators.InputRequired()]
    )
    payment_plan = SelectField('Desired Payment Plan')


class BaseMotorForm(BaseProductForm):
    motor_model = StringField('Vehicle Model?', [
        validators.InputRequired()
    ])
    motor_make = StringField('Vehicle Make?', [
        validators.InputRequired()
    ])
    motor_year_of_manufacture = SelectField(
        'Vehicle year of manufacture ?', [validators.InputRequired()]
    )
    motor_use = StringField('Vehicle Use', [
        validators.InputRequired()
    ])
    motor_policy_type = SelectField("Motor Policy Type")
    recent_profesional_evaluation = BooleanField("Has the vehicle been \
        professionally valued in the last 18 months?")


class CompleteMotorForm(BaseMotorForm):
    motor_seating_capacity = IntegerField(
        'Vehicle Seating Capacity ?', [validators.InputRequired()]
    )
    motor_registration_number = StringField('Vehicle Registration Number', [
        validators.InputRequired()
    ])
    motor_engine_number = StringField('Vehicle Engine Number', [
        validators.InputRequired()
    ])
    motor_engine_cc = IntegerField('Vehicle Engine CC', [
        validators.InputRequired()
    ])


class MotorPrivateCoverForm(CompleteMotorForm):
    policy_status = SelectField("Policy Status")
    policy_expiry_date = DateField(
        'Policy Expiry Date',
        [validators.InputRequired()]
    )
    policy_number = ('Policy Number', [
        validators.InputRequired()
    ])
    policy_underwriter = ('Policy Underwriter', [
        validators.InputRequired()
    ])
