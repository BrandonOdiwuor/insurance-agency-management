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
