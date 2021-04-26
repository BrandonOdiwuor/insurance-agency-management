from app import db
from app.models.user import User
from app.models.customer import Customer, CustomerStatus
from app.models.invoice import Invoice
from app.models.payment import Payment
from app.models.quotation import MotorPrivateQuotation, MotorCommercialQuotation, \
    Quotation, MedicalInpatientQuotation, MedicalOutpatientQuotation
from app.models.sale_item import SaleItem
from app.models.policy import Policy, PrivateMotorPolicy, CommercialMotorPolicy, \
    MedicalInpatientPolicy
from app.utils.utils import private_motor_premium_claculator, \
    commercial_motor_premium_claculator, medical_inpatient_premium_claculator, \
        medical_outpatient_premium_claculator
from app.utils.enums import ProductTypes


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
    return Quotation.query.filter_by(
        customer_id=customer_id
    ).all()


def get_customer_policies(customer_id):
    return Policy.query.filter_by(
        customer_id=customer_id
    ).all()


def get_customer_info(customer_id):
    customer = get_customer(customer_id)
    invoices = get_customer_invoices(customer_id)
    payments = get_customer_payments(customer_id)
    policies = get_customer_policies(customer_id)
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
    invoice = Invoice(**invoice_payload)

    try:
        db.session.add(invoice)
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


def create_policy(policy_payload):
    policy = None
    if policy_payload['product_type'] == ProductTypes.MOTOR_PRIVATE:
        policy = PrivateMotorPolicy(**policy_payload)
        policy.premium = private_motor_premium_claculator(
            float(policy.sum_insured)
        )
    elif policy_payload['product_type'] == ProductTypes.MOTOR_COMMERCIAL:
        policy = CommercialMotorPolicy(**policy_payload)
        policy.premium = commercial_motor_premium_claculator(
            float(policy.sum_insured)
        )
    elif policy_payload['product_type'] == ProductTypes.MEDICAL_INPATIENT:
        policy = MedicalInpatientPolicy(**policy_payload)
        policy.premium = medical_inpatient_premium_claculator(
            float(policy.sum_insured)
        )
    policy.premium = round(policy.premium, 2)
    try:
        db.session.add(policy)
        db.session.commit()

    except Exception as exception:
        print("error : ", exception)


def get_policies():
    return Policy.query.all()


def get_policy(policy_id):
    return Policy.query.filter_by(
        id=policy_id
    ).first()


def update_policy(policy_id, policy_payload):
    policy = Policy.query.filter_by(
        id=policy_id
    ).first()

    if policy:
        for key in policy_payload:
            setattr(policy, key, policy_payload[key])
            
        if policy.product_type == ProductTypes.MOTOR_PRIVATE:
            policy.premium = private_motor_premium_claculator(
                float(policy.sum_insured)
            )
        else:
            policy.premium = commercial_motor_premium_claculator(
                float(policy.sum_insured)
            )
        policy.premium = round(policy.premium, 2)
        try:
            db.session.commit()

        except Exception as exception:
            print("error : ", exception)


def create_quote(quotation_payload):
    quotation = None
    product_type = quotation_payload['product_type']
    print(product_type)
    if product_type == ProductTypes.MOTOR_PRIVATE:
        quotation = MotorPrivateQuotation(**quotation_payload)
        quotation.premium = private_motor_premium_claculator(
            float(quotation.sum_insured)
        )
    elif product_type == ProductTypes.MOTOR_COMMERCIAL:
        quotation = MotorCommercialQuotation(**quotation_payload)
        quotation.premium = commercial_motor_premium_claculator(
            float(quotation.sum_insured)
        )
    elif product_type == ProductTypes.MEDICAL_INPATIENT:
        quotation = MedicalInpatientQuotation(**quotation_payload)
        quotation.premium = medical_inpatient_premium_claculator(
            float(quotation.sum_insured)
        )
    elif product_type == ProductTypes.MEDICAL_OUTPATIENT:
        quotation = MedicalOutpatientQuotation(**quotation_payload)
        quotation.premium = medical_outpatient_premium_claculator(
            float(quotation.sum_insured)
        )
    quotation.premium = round(quotation.premium, 2)
    try:
        db.session.add(quotation)
        db.session.commit()

    except Exception as exception:
        print("error : ", exception)


def get_quote(quotation_id):
    return Quotation.query.filter_by(
        id=quotation_id
    ).first()


def get_quotes():
    return Quotation.query.all()


def update_quote(quotation_id, quotation_payload):
    quotation = Quotation.query.filter_by(
        id=quotation_id
    ).first()
    if quotation:
        for key in quotation_payload:
            setattr(quotation, key, quotation_payload[key])
        if quotation.product_type == ProductTypes.MOTOR_PRIVATE:
            quotation.premium = private_motor_premium_claculator(
                float(quotation.sum_insured)
            )
        elif quotation.product_type == ProductTypes.MOTOR_COMMERCIAL:
            quotation.premium = commercial_motor_premium_claculator(
                float(quotation.sum_insured)
            )
        elif quotation.product_type == ProductTypes.MEDICAL_INPATIENT:
            quotation.premium = medical_inpatient_premium_claculator(
                float(quotation.sum_insured)
            )
        elif quotation.product_type == ProductTypes.MEDICAL_OUTPATIENT:
            quotation.premium = medical_outpatient_premium_claculator(
                float(quotation.sum_insured)
            )
        quotation.premium = round(quotation.premium, 2)
        try:
            db.session.commit()

        except Exception as exception:
            print("error : ", exception)
