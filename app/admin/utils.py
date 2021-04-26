from .forms import MotorQuotationForm, MotorPolicyForm
from app.utils.enums import MotorPolicyTypes, PaymentPlans, PolicyStatus


def baseMotorForm(form):
    form.motor_policy_type.choices = [
        (policy_type.name, policy_type.value) for policy_type in MotorPolicyTypes
    ]
    form.motor_year_of_manufacture.choices = [
        (year, year) for year in range(1995, 2022)
    ]
    form.payment_plan.choices = [
        (payment_plan.name, payment_plan.value) for payment_plan in PaymentPlans
    ]
    return form


def motorQuotationForm(form):
    return baseMotorForm(form)


def medicalQuotationForm(form):
    form.payment_plan.choices = [
        (payment_plan.name, payment_plan.value) for payment_plan in PaymentPlans
    ]
    return form


def motorPolicyForm(motor_policy_form):
    policy_form = baseMotorForm(motor_policy_form)
    policy_form.policy_status.choices = [
        (policy_status.name, policy_status.value) for policy_status in PolicyStatus
    ]
    return policy_form


def medicalPolicyForm(form):
    form.payment_plan.choices = [
        (payment_plan.name, payment_plan.value) for payment_plan in PaymentPlans
    ]
    form.policy_status.choices = [
        (policy_status.name, policy_status.value) for policy_status in PolicyStatus
    ]
    return form
