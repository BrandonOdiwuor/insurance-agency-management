from enum import Enum


class CustomerStatus(Enum):
    ACTIVE = "Active"
    INACTIVE = "InActive"


class InvoiceStatus(Enum):
    ACTIVE = "Active"
    PAID = "Paid"
    OVERDUE = "Overdue"


class PaymentModes(Enum):
    CASH = "Cash"
    M_PESA = "M-Pesa"


class GenderChoices(Enum):
    Male = "Male"
    Female = "Female"


class CoverTypes(Enum):
    MOTOR_COMMERCIAL = "Motor Commercial"
    MOTOR_PRIVATE = "Motor Private"
    MEDICAL_INPATIENT = "Medical Inpatient"
    MEDICAL_OUTPATIEN = "Medial Outpatient"


class QuotationTypes(Enum):
    MOTOR_COMMERCIAL = "Motor Commercial"
    MOTOR_PRIVATE = "Motor Private"
    MEDICAL_INPATIENT = "Medical Inpatient"
    MEDICAL_OUTPATIEN = "Medial Outpatient"


class ProductTypes(Enum):
    MOTOR_COMMERCIAL = "Motor Commercial"
    MOTOR_PRIVATE = "Motor Private"
    MEDICAL_INPATIENT = "Medical Inpatient"
    MEDICAL_OUTPATIEN = "Medial Outpatient"


class PaymentPlans(Enum):
    MONTHLY = "Monthly Payment"
    QUARTERLY = "Quarterly payment"
    SEMI_ANNUALLY = "Semi-annual payment"
    ANNUALLY = "Annual Payment"


class MotorPolicyTypes(Enum):
    COMPREHENSIVE = "Motor Comprehensive"
    THIRD_PARTY = "Motor 3rd party"


class PolicyStatus(Enum):
    CREATED = "Created"
    INVOICE_SENT = "Invoice Sent"
    INVOICE_PAID = "Invoice Partially Paid"
    INVOICE_PAYMENT_COMPLETE = "Invoice Payment Complete"
    POLICY_ACTIVE = "Policy Active"

