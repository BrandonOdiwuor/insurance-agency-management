from flask_wtf import FlaskForm
from wtforms import StringField, SelectField, \
    HiddenField, validators
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


class QuotationForm(FlaskForm):
    quotation_type = HiddenField(
        'quotation_type', [validators.InputRequired()]
    )
    cover_start_date = DateField(
        'When do you want your cover to start?',
        [validators.InputRequired()]
    )
    sum_insured = DecimalField(
        'Insurable Amount(Ksh.)', [validators.InputRequired()]
    )
    payment_plan = SelectField('Desired Payment Plan')


class MotorQuotation(QuotationForm):
    vehicle_model = StringField('Vehicle Model?', [
        validators.InputRequired()
    ])
    year_of_manufacture = DateField(
        'Vehicle year of manufacture ?', [validators.InputRequired()]
    )
    motor_use = StringField('Vehicle Use', [
        validators.InputRequired()
    ])
    motor_cover_type = SelectField("Motor Cover Type")


# class MotorPrivateQuotation(MotorQuotation):
#     pass


class MotorCommercialQuotation(MotorQuotation):
    vehicle_type = StringField('Vehicle Type', [
        validators.InputRequired()
    ])
