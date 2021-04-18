from app import db
from app.models.user import User
from app.models.customer import Customer, CustomerStatus
from app.models.invoice import Invoice, InvoiceStatus
from app.models.payment import Payment
from app.models.covers import Cover
from app.models.quotation import MotorPrivateQuotation
from app.models.sale_item import SaleItem
from app.utils.utils import private_motor_premium_claculator
from app.utils.enums import QuotationTypes


def create_user(user_payload):
    new_user = User(
        email=user_payload['email'],
        password=user_payload['password'],
        phone=user_payload['phone'],
        f_name=user_payload['first_name'],
        l_name=user_payload['last_name']
    )

    try:
        db.session.add(new_user)
        db.session.commit()
    except Exception as exception:
        print("error : ", exception)


def verify_user(email, password):
    user = User.query.filter_by(email=email).first()

    if user and user.verify_password(password):
        return user

    return False


def create_item_of_sale(item_payload):
    new_item = SaleItem(
        category=item_payload['category'],
        name=item_payload['name'],
        price=item_payload['price']
    )

    try:
        db.session.add(new_item)
        db.session.commit()

    except Exception as exception:
        print("error : ", exception)


def get_items_of_sale():
    return SaleItem.query.all()


def create_customer(customer_payload):
    customer = Customer(
        first_name=customer_payload['first_name'],
        last_name=customer_payload['last_name'],
        national_id_number=customer_payload['national_id_number'],
        primary_phone_number=customer_payload['primary_phone_number'],
        primary_email=customer_payload['primary_email'],
        password=customer_payload['password'],
        account_status=CustomerStatus.INACTIVE,
        physical_address=customer_payload['physical_address'],
        city=customer_payload['city'],
        county=customer_payload['county'],
        postal_address=customer_payload['postal_address'],
        postal_code=customer_payload['postal_code'],
        gender=customer_payload['gender'],
        birth_date=customer_payload['birth_date'],
        kra_pin=customer_payload['kra_pin'],
        attachment_id_front=customer_payload['attachment_id_front'],
        attachment_id_back=customer_payload['attachment_id_front']
    )

    try:
        db.session.add(customer)
        db.session.commit()

    except Exception as exception:
        print("error : ", exception)


def verify_customer(email, password):
    customer = Customer.query.filter_by(email=email).first()

    if customer and customer.verify_password(password):
        return customer

    return False


def get_customers():
    return Customer.query.all()


def get_customer(customer_id):
    return Customer.query.filter_by(id=customer_id).first()


def get_customer_quotations(customer_id):
    return MotorPrivateQuotation.query.filter_by(
        customer_id=customer_id
    ).all()


def get_customer_info(customer_id):
    customer = get_customer(customer_id)
    invoices = get_customer_invoices(customer_id)
    payments = get_customer_payments(customer_id)
    policies = []
    quotations = get_customer_quotations(customer_id)

    return dict(
        customer=customer,
        invoices=invoices,
        payments=payments,
        policies=policies,
        quotations=quotations
    )


def validate_customer_email(email):
    return Customer.query.filter_by(primary_email=email).first()


def validate_customer_telephone(telephone):
    return Customer.query.filter_by(primary_phone_number=telephone).first()


def update_customer_status(customer_id):
    customer = Customer.query.filter_by(id=customer_id).first()

    if customer.account_status == CustomerStatus.ACTIVE:
        customer.account_status = CustomerStatus.INACTIVE
    else:
        customer.account_status = CustomerStatus.ACTIVE
    try:
        db.session.commit()

    except Exception as exception:
        print("error : ", exception)


def edit_customer(customer_id, customer_payload):
    customer = Customer.query.filter_by(id=customer_id).first()
    for key in customer_payload:
        setattr(customer, key, customer_payload[key])

    try:
        db.session.commit()

    except Exception as exception:
        print("error : ", exception)


def create_invoice(invoice_payload):
    new_invoice = Invoice(
        item_id=invoice_payload['item'],
        customer_id=invoice_payload['customer'],
        price=invoice_payload['price'],
        due_at=invoice_payload['due_at'],
        status=InvoiceStatus.ACTIVE
    )

    try:
        db.session.add(new_invoice)
        db.session.commit()

    except Exception as exception:
        print("error : ", exception)


def update_invoice_status(invoice_id, status):
    invoice = Invoice.query.filter_by(id=invoice_id).first()
    invoice.status = status

    try:
        db.session.commit()

    except Exception as exception:
        print("error : ", exception)


def get_invoice(invoice_id):
    return Invoice.query.filter_by(id=invoice_id).first()


def get_customer_invoices(customer_id):
    return Invoice.query.filter_by(customer_id=customer_id).all()


def get_invoices():
    return Invoice.query.all()


def create_payment(payment_payload):
    new_payment = Payment(
        invoice_id=payment_payload['invoice'],
        amount=payment_payload['amount'],
        payment_mode=payment_payload['payment_mode']
    )

    try:
        db.session.add(new_payment)
        db.session.commit()

    except Exception as exception:
        print("error : ", exception)


def get_payment(payment_id):
    return Payment.query.filter_by(id=payment_id).first()


def get_payments():
    return Payment.query.all()


def get_customer_payments(customer_id):
    return Payment.query.join(Invoice).join(
        Customer, Invoice.customer_id == Customer.id
    ).filter_by(id=customer_id).all()

# def create_cover:
#     pass

# def get_cover:
#     pass


def create_motor_private_quote(quotation_payload):
    quotation = MotorPrivateQuotation(**quotation_payload)
    quotation.calculated_premium = private_motor_premium_claculator(
        float(quotation.sum_insured)
    )
    try:
        db.session.add(quotation)
        db.session.commit()

    except Exception as exception:
        print("error : ", exception)


def get_quote(quotation_type, quotation_id):
    quotation = None
    if quotation_type == QuotationTypes.MOTOR_PRIVATE.name:
        quotation = MotorPrivateQuotation.query.filter_by(
            id=quotation_id
        ).first()
    return quotation


def update_quote(quotation_type, quotation_id, quotation_payload):
    quotation = None
    if quotation_type == QuotationTypes.MOTOR_PRIVATE.name:
        quotation = MotorPrivateQuotation.query.filter_by(
            id=quotation_id
        ).first()
    
    if quotation:
        for key in quotation_payload:
            setattr(quotation, key, quotation_payload[key])
        quotation.calculated_premium = private_motor_premium_claculator(
            float(quotation.sum_insured)
        )
        try:
            db.session.commit()

        except Exception as exception:
            print("error : ", exception)
