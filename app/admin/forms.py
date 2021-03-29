from flask_wtf import FlaskForm
from wtforms import StringField, SelectField, \
    HiddenField, validators
from wtforms.fields.html5 import DateTimeLocalField, DecimalField


class SaleItemForm(FlaskForm):
    name = StringField('Name', [
        validators.InputRequired()])
    category = StringField('Category', [
        validators.InputRequired(),
        validators.Length(max=10)
    ])
    price = DecimalField('Price', [validators.InputRequired()])


class CustomerInvoiceForm(FlaskForm):
    due_at = DateTimeLocalField('Due date', [
        validators.InputRequired()])
    price = DecimalField('Price', [validators.InputRequired()])
    item = SelectField('Product')


class CustomerInvoicePaymentForm(FlaskForm):
    invoice_id = HiddenField('invoice_id', [validators.InputRequired()])
    amount = DecimalField('Amount', [validators.InputRequired()])
    payment_mode = SelectField('Payment Mode')
