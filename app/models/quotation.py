from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy import text
from app.models import Base
from app.models.mixins.motor_mixins import MotorMixin
from app import db
from app.utils.enums import ProductTypes


class Quotation(Base, MotorMixin):

    __tablename__ = 'quotations'

    product_type = db.Column(
        db.Enum(ProductTypes), nullable=False
    )
    customer_id = db.Column(
        UUID(as_uuid=True),
        db.ForeignKey('customers.id'),
        nullable=False
    )

    __mapper_args__ = {
        'polymorphic_on': product_type
    }


class MotorPrivateQuotation(Quotation):

    __tablename__ = 'motor_private_quotations'

    id = db.Column(
        UUID(as_uuid=True), 
        db.ForeignKey('quotations.id'),
        primary_key=True, 
        server_default=text("uuid_generate_v4()")
    )

    __mapper_args__ = {
        'polymorphic_identity': ProductTypes.MOTOR_PRIVATE,
    }

    def __repr__(self):
        return '<Quotation %r>' % (self.id)


class MotorCommercialQuotation(Quotation):

    __tablename__ = 'motor_commercial_quotations'

    id = db.Column(
        UUID(as_uuid=True), 
        db.ForeignKey('quotations.id'),
        primary_key=True, 
        server_default=text("uuid_generate_v4()")
    )

    __mapper_args__ = {
        'polymorphic_identity': ProductTypes.MOTOR_COMMERCIAL,
    }

    def __repr__(self):
        return '<Quotation %r>' % (self.id)
