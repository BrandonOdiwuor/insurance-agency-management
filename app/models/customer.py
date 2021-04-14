from werkzeug.security import generate_password_hash, check_password_hash
from app.models import Base
from app import db
from app.utils.enums import CustomerStatus


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
