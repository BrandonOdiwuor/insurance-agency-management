from werkzeug.security import generate_password_hash, check_password_hash
from app.models import Base
from app import db
from app.utils.enums import CustomerStatus, GenderChoices


class Customer(Base):

    __tablename__ = 'customers'

    first_name = db.Column(db.String(255), nullable=False)
    last_name = db.Column(db.String(255),  nullable=False)
    national_id_number = db.Column(db.String(8), unique=True,  nullable=False)
    primary_email = db.Column(db.String(100), unique=True, nullable=False)
    primary_phone_number = db.Column(db.String(9), unique=True, nullable=False)
    account_status = db.Column(db.Enum(CustomerStatus), nullable=False)
    password_hash = db.Column(db.String(200), nullable=False)
    physical_address = db.Column(db.String(255), nullable=False)
    city = db.Column(db.String(255), nullable=False)
    county = db.Column(db.String(255), nullable=False)
    postal_address = db.Column(db.String(255), nullable=False)
    postal_code = db.Column(db.String(255), nullable=False)
    gender = db.Column(db.Enum(GenderChoices), nullable=False)
    birth_date = db.Column(db.DateTime, nullable=False)
    kra_pin = db.Column(db.String(255), nullable=False)
    attachment_id_front = db.Column(db.String(255), nullable=False)
    attachment_id_back = db.Column(db.String(255), nullable=False)
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
        return self.account_status == CustomerStatus.ACTIVE
