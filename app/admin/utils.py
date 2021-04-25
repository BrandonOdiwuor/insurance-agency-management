from .forms import BaseMotorForm
from app.utils.enums import MotorPolicyTypes, PaymentPlans

def motorQuotationForm(product_type):
    quotation_form = BaseMotorForm(
        product_type=product_type
    )
    quotation_form.motor_policy_type.choices = [
        (policy_type.name, policy_type.value) for policy_type in MotorPolicyTypes
    ]
    quotation_form.motor_year_of_manufacture.choices = [
        (year, year) for year in range(1995, 2022)
    ]
    quotation_form.payment_plan.choices = [
        (payment_plan.name, payment_plan.value) for payment_plan in PaymentPlans
    ]
    return quotation_form