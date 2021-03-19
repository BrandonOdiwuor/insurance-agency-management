from enum import Enum


class CustomerStatus(Enum):
    ACTIVE = "Active"
    INACTIVE = "InActive"

class InvoiceStatus(Enum):
    ACTIVE = "Active"
    PAID = "Paid"
    OVERDUE = "Overdue"