from app.models import Base
from app import db
from app.utils.enums import InvoiceStatus


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
