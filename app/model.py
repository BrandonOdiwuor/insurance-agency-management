from enum import Enum
from app import db, JWT_SECRET_KEY, JWT_TOKEN_LIFE_IN_SECONDS
from datetime import datetime, timedelta
import jwt

class Base(db.Model):
    __abstract__ = True
    id = db.Column(db.Integer, primary_key=True)
    created_at = db.Column(db.DateTime,  default=db.func.current_timestamp())
    updated_at = db.Column(db.DateTime,  default=db.func.current_timestamp(),
                                           onupdate=db.func.current_timestamp())

class CustomerStatus(Enum):
    ACTIVE = "Active"
    INACTIVE = "InActive"

class InvoiceStatus(Enum):
    ACTIVE = "Active"
    PAID = "Paid"
    OVERDUE = "Overdue"

class Customer(Base):

    __tablename__ = 'customers'

    f_name = db.Column(db.String(20), nullable=False)
    l_name = db.Column(db.String(20),  nullable=False)
    id_no = db.Column(db.String(8), unique=True,  nullable=False)
    email = db.Column(db.String(100), unique=True, nullable=False)
    phone = db.Column(db.String(9), unique=True, nullable=False)
    status = db.Column(db.Enum(CustomerStatus), nullable=False)
    password_hash = db.Column(db.String(200), nullable=False)

    def __repr__(self):
        return '<Customer %r>' % (self.email) 

class User(Base):

    __tablename__ = 'users'

    f_name = db.Column(db.String(20), nullable=False)
    l_name = db.Column(db.String(20),  nullable=False)
    email = db.Column(db.String(100), unique=True, nullable=False)
    password_hash = db.Column(db.String(200), nullable=False)
    user_type = db.Column(db.String(20))
    phone = db.Column(db.String(9), unique=True, nullable=False)


    def token(self):
        generated = datetime.now()
        expiry = datetime.now() + timedelta(seconds=JWT_TOKEN_LIFE_IN_SECONDS)

        token = jwt.encode(
            {
                "uid": str(self.id),
                "exp": int(expiry.strftime("%s")),
                "iat": int(generated.strftime("%s")),
            },
            JWT_SECRET_KEY,
            algorithm="HS256",
        )

        return token

    def __repr__(self):
        return '<User %r>' % (self.email) 
    
class SaleItem(Base):

    __tablename__ = 'sale_items'

    name = db.Column(db.String(20))
    category = db.Column(db.String(10))
    price = db.Column(db.Float)
    item_quote_procedure_json = db.Column(db.JSON)
    details_json = db.Column(db.JSON)

    def __repr__(self):
        return '<Product %r>' % (self.name) 

class Invoice(Base):

    __tablename__ = 'invoices'

    item_id = db.Column(db.Integer, db.ForeignKey('sale_items.id'), nullable=False)
    customer_id = db.Column(db.Integer, db.ForeignKey('customers.id'), nullable=False)
    price = db.Column(db.Float, nullable=False)
    status = db.Column(db.Enum(InvoiceStatus), nullable=False)
    due_at = db.Column(db.DateTime,  default=db.func.current_timestamp() + \
                                            timedelta(days = 1))

    def __repr__(self):
        return '<Invoice %r>' % (self.id)

class Payment(Base):

    __tablename__ = 'payments'

    invoice_id = db.Column(db.Integer)
    amount = db.Column(db.Float)
    payment_json = db.Column(db.JSON)

    def __repr__(self):
        return '<Payment %r>' % (self.id)

class Policy(Base):

    __tablename__ = 'policies'

    customer_id = db.Column(db.Integer)

    def __repr__(self):
        return '<Policy %r>' % (self.id)

class Quotation(Base):

    __tablename__ = 'quotations'

    client_email = db.Column(db.String(100), unique=True, nullable=False)
    client_phone = db.Column(db.String(9), unique=True, nullable=False)
    item_id = db.Column(db.Integer)

    def __repr__(self):
        return '<Quotation %r>' % (self.id)