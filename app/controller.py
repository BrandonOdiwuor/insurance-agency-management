from app import db
from app.model import User, Customer, CustomerStatus, Invoice, \
    InvoiceStatus, Payment, Policy, Quotation, SaleItem

def create_user(user_payload):
    new_user = User(
        email=user_payload['email'], 
        password_hash=generate_password_hash(user_payload['password']),
        phone=user_payload['phone'],
        f_name = user_payload['first_name'],
        l_name = user_payload['last_name']
    )

    try:
        db.session.add(new_user)
        db.session.commit()
    except Exception as exception:
        print("error : ", exception)

def verify_user(email, password):
    user = User.query.filter_by(email=email).first()

    if user and check_password_hash(user.password_hash, password):
        return user
    
    return False

def create_item_of_sale(item_payload):
    new_item = SaleItem(
        category = item_payload['category'],
        name = item_payload['name'],
        price = item_payload['price']
    )
    
    try:
        db.session.add(new_item)
        db.session.commit()
       
    except Exception as exception:
        print("error : ",exception)

def create_customer(customer_payload):
    new_customer = Customer(
        f_name = customer_payload['first_name'],
        l_name = customer_payload['last_name'],
        id_no = customer_payload['id_no'],
        phone = customer_payload['phone'],
        email = customer_payload['email'],
        password_hash=generate_password_hash(customer_payload['password']),
        status = CustomerStatus.INACTIVE
    )
    
    try:
        db.session.add(new_customer)
        db.session.commit()
       
    except Exception as exception:
        print("error : ",exception)

def verify_customer(email, password):
    customer = Customer.query.filter_by(email=email).first()

    if customer and check_password_hash(customer.password_hash, password):
        return customer
    
    return False

def get_customer(customer_id):
    return Customer.query.filter_by(id=customer_id).first()

def activate_customer(customer_id):
    customer = Customer.query.filter_by(id=customer_id).first()
    customer.status = CustomerStatus.ACTIVE
    
    try:
        db.session.commit()
       
    except Exception as exception:
        print("error : ",exception)

def deactivate_customer(customer_id):
    customer = Customer.query.filter_by(id=customer_id).first()
    customer.status = CustomerStatus.INACTIVE
    
    try:
        db.session.commit()
       
    except Exception as exception:
        print("error : ",exception)

def create_invoice(invoice_payload):
    new_invoice = Invoice(
        item_id = invoice_payload['item'],
        customer_id = invoice_payload['customer'],
        price = invoice_payload['price'],
        status = InvoiceStatus.ACTIVE
    )
    
    try:
        db.session.add(new_invoice)
        db.session.commit()
       
    except Exception as exception:
        print("error : ",exception)

def update_invoice_status(invoice_id, status):
    invoice = Invoice.query.filter_by(id=invoice_id).first()
    invoice.status = status
    
    try:
        db.session.commit()
       
    except Exception as exception:
        print("error : ",exception)

def get_invoice(invoice_id):
    return Invoice.query.filter_by(id=invoice_id).first()

def create_payment(payment_payload):
    new_payment = Payment(
        invoice_id = payment_payload['invoice'],
        amount = payment_payload['amount'],
        status = payment_payload['status']
    )
    
    try:
        db.session.add(new_payment)
        db.session.commit()
       
    except Exception as exception:
        print("error : ",exception)

def get_payment(payment_id):
    return Payment.query.filter_by(id=payment_id).first()

# def create_cover:
#     pass

# def get_cover:
#     pass

# def create_quote(quote_payload):
#     # new_quote = Payment(
#     #     invoice_id = invoice_payload['invoice'],
#     #     amount = invoice_payload['amount'],
#     #     status = invoice_payload['status']
#     # )
    
#     # try:
#     #     db.session.add(new_quote)
#     #     db.session.commit()
       
#     # except Exception as exception:
#     #     print("error : ",exception)

# def get_quote:
#     pass