from flask_wtf import FlaskForm
from wtforms import StringField, SelectField, \
    HiddenField, validators
from wtforms.fields.html5 import DateTimeLocalField, DecimalField


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
