from sqlalchemy.dialects.postgresql import UUID
from app.models import Base
from app import db
from app.utils.enums import PaymentModes


class Payment(Base):

    __tablename__ = 'payments'

    invoice_id = db.Column(
        UUID(as_uuid=True),
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
