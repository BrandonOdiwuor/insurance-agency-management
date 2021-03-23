from flask_wtf import FlaskForm
from wtforms import StringField, DecimalField, validators

class SaleItemForm(FlaskForm):
    name = StringField('Name', [
        validators.InputRequired()])
    category = StringField('Category', [
        validators.InputRequired(),
        validators.Length(max=10)
    ])
    price = DecimalField('Price', [validators.InputRequired()])