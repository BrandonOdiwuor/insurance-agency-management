from sqlalchemy.dialects.postgresql import UUID
from app.models import Base
from app import db
from app.utils.enums import PaymentPlans, QuotationTypes, MotorCoverTypes


class QuotationMixin(object):
    quotation_type = db.Column(
        db.Enum(QuotationTypes), nullable=False
    )
    cover_start_date = db.Column(
        db.DateTime,  default=db.func.current_timestamp()
    )
    sum_insured = db.Column(db.Float, nullable=False)
    payment_plan = db.Column(db.Enum(PaymentPlans), nullable=False)
    calculated_premium = db.Column(db.Float, nullable=False)


class MotorQuotationMixin(QuotationMixin):
    vehicle_model = db.Column(db.String(255), nullable=False)
    year_of_manufacture = db.Column(
        db.DateTime,  default=db.func.current_timestamp()
    )
    motor_use = db.Column(db.String(255), nullable=False)
    motor_cover_type = db.Column(db.Enum(MotorCoverTypes), nullable=False)


class MotorPrivateQuotation(Base, MotorQuotationMixin):

    __tablename__ = 'motor_private_quotations'

    customer_id = db.Column(
        UUID(as_uuid=True),
        db.ForeignKey('customers.id'),
        nullable=False
    )

    def __repr__(self):
        return '<Quotation %r>' % (self.id)


class MotorCommercialQuotation(Base, MotorQuotationMixin):

    __tablename__ = 'motor_commercial_quotations'

    customer_id = db.Column(
        UUID(as_uuid=True),
        db.ForeignKey('customers.id'),
        nullable=False
    )

    def __repr__(self):
        return '<Quotation %r>' % (self.id)
