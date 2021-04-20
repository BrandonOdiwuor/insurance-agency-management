from sqlalchemy.dialects.postgresql import UUID
from app.models import Base
from app import db
from app.utils.enums import InvoiceStatus


class Invoice(Base):

    __tablename__ = 'invoices'

    policy_id = db.Column(
        UUID(as_uuid=True), 
        db.ForeignKey('policies.id'), nullable=False
    )
    customer_id = db.Column(
        UUID(as_uuid=True), 
        db.ForeignKey('customers.id'), nullable=False
    )
    amount = db.Column(db.Float, nullable=False)
    status = db.Column(db.Enum(InvoiceStatus), nullable=False)
    due_date = db.Column(db.DateTime,  default=db.func.current_timestamp())
    payments = db.relationship('Payment', backref='invoice', lazy=True)

    def __repr__(self):
        return '<Invoice %r>' % (self.id)
