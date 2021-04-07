from os import environ
from datetime import datetime, timedelta
from werkzeug.security import generate_password_hash, check_password_hash
import jwt
from app import db
from app.utils.enums import CustomerStatus, InvoiceStatus, PaymentModes


class Base(db.Model):
    __abstract__ = True
    id = db.Column(db.Integer, primary_key=True)
    created_at = db.Column(db.DateTime,  default=db.func.current_timestamp())
    updated_at = db.Column(db.DateTime,  default=db.func.current_timestamp(),
                           onupdate=db.func.current_timestamp())


class Customer(Base):

    __tablename__ = 'customers'

    f_name = db.Column(db.String(20), nullable=False)
    l_name = db.Column(db.String(20),  nullable=False)
    id_no = db.Column(db.String(8), unique=True,  nullable=False)
    email = db.Column(db.String(100), unique=True, nullable=False)
    phone = db.Column(db.String(9), unique=True, nullable=False)
    status = db.Column(db.Enum(CustomerStatus), nullable=False)
    password_hash = db.Column(db.String(200), nullable=False)
    invoices = db.relationship('Invoice', backref='customer', lazy=True)

    @property
    def password(self):
        """
        Prevent pasword from being accessed
        """
        raise AttributeError('password is not a readable attribute.')

    @password.setter
    def password(self, password):
        """
        Set password to a hashed password
        """
        self.password_hash = generate_password_hash(password)

    def verify_password(self, password):
        """
        Check if hashed password matches actual password
        """
        return check_password_hash(self.password_hash, password)

    def __repr__(self):
        return '<Customer %r>' % (self.email)

    def is_active(self):
        return self.status == CustomerStatus.ACTIVE


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
        expiry = datetime.now() + timedelta(seconds=int(environ.get('JWT_TOKEN_LIFE_IN_SECONDS')))

        token = jwt.encode(
            {
                "uid": str(self.id),
                "exp": int(expiry.strftime("%s")),
                "iat": int(generated.strftime("%s")),
            },
            environ.get('JWT_SECRET_KEY'),
            algorithm="HS256",
        )

        return token

    @property
    def password(self):
        """
        Prevent pasword from being accessed
        """
        raise AttributeError('password is not a readable attribute.')

    @password.setter
    def password(self, password):
        """
        Set password to a hashed password
        """
        self.password_hash = generate_password_hash(password)

    def verify_password(self, password):
        """
        Check if hashed password matches actual password
        """
        return check_password_hash(self.password_hash, password)

    def __repr__(self):
        return '<User %r>' % (self.email)


class SaleItem(Base):

    __tablename__ = 'sale_items'

    name = db.Column(db.String(20))
    category = db.Column(db.String(20))
    price = db.Column(db.Float)
    item_quote_procedure_json = db.Column(db.JSON)
    details_json = db.Column(db.JSON)

    def __repr__(self):
        return '<Product %r>' % (self.name)


class Invoice(Base):

    __tablename__ = 'invoices'

    item_id = db.Column(db.Integer, db.ForeignKey(
        'sale_items.id'), nullable=False)
    customer_id = db.Column(db.Integer, db.ForeignKey(
        'customers.id'), nullable=False)
    price = db.Column(db.Float, nullable=False)
    status = db.Column(db.Enum(InvoiceStatus), nullable=False)
    due_at = db.Column(db.DateTime,  default=db.func.current_timestamp())
    payments = db.relationship('Payment', backref='invoice', lazy=True)

    def __repr__(self):
        return '<Invoice %r>' % (self.id)


class Payment(Base):

    __tablename__ = 'payments'

    invoice_id = db.Column(
        db.Integer, 
        db.ForeignKey('invoices.id')
    )
    amount = db.Column(db.Float)
    payment_mode = db.Column(
        db.Enum(PaymentModes), 
        default=PaymentModes.M_PESA
    )
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
