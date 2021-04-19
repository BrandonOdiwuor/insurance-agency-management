from sqlalchemy.dialects.postgresql import UUID
from app.models import Base
from app.models.mixins.motor_mixins import MotorMixin
from app import db


class MotorPrivateQuotation(Base, MotorMixin):

    __tablename__ = 'motor_private_quotations'

    customer_id = db.Column(
        UUID(as_uuid=True),
        db.ForeignKey('customers.id'),
        nullable=False
    )

    def __repr__(self):
        return '<Quotation %r>' % (self.id)


class MotorCommercialQuotation(Base, MotorMixin):

    __tablename__ = 'motor_commercial_quotations'

    customer_id = db.Column(
        UUID(as_uuid=True),
        db.ForeignKey('customers.id'),
        nullable=False
    )

    def __repr__(self):
        return '<Quotation %r>' % (self.id)
