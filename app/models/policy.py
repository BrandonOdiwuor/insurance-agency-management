from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy import text
from app.models import Base
from app.models.mixins.motor_mixins import MotorPolicyMixin
from app import db
from app.utils.enums import ProductTypes


class Policy(Base, MotorPolicyMixin):

    __tablename__ = 'policies'

    product_type = db.Column(
        db.Enum(ProductTypes), nullable=False
    )
    customer_id = db.Column(
        UUID(as_uuid=True),
        db.ForeignKey('customers.id'),
        nullable=False
    )
    invoices = db.relationship('Invoice', backref='policy', lazy=True)

    __mapper_args__ = {
        'polymorphic_on': product_type
    }


class PrivateMotorPolicy(Policy):

    __tablename__ = 'private_motor_policies'

    id = db.Column(
        UUID(as_uuid=True), 
        db.ForeignKey('policies.id'),
        primary_key=True, 
        server_default=text("uuid_generate_v4()")
    )
    log_book_attachment = db.Column(db.String(255), nullable=False)

    __mapper_args__ = {
        'polymorphic_identity': ProductTypes.MOTOR_PRIVATE,
    }

    def __repr__(self):
        return '<MotorPrivatePolicy %r>' % (self.id)