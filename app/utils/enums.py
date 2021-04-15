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