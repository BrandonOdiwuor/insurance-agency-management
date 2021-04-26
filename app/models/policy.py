from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy import text
from app.models import Base
from app.models.mixins.motor_mixins import MotorMixin
from app.models.mixins.medical_mixins import MedicalMixin
from app.models.mixins import BasePolicyMixin
from app import db
from app.utils.enums import ProductTypes


class Policy(Base, BasePolicyMixin):

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


class PrivateMotorPolicy(Policy, MotorMixin):

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


class CommercialMotorPolicy(Policy, MotorMixin):

    __tablename__ = 'commercial_motor_policies'

    id = db.Column(
        UUID(as_uuid=True),
        db.ForeignKey('policies.id'),
        primary_key=True,
        server_default=text("uuid_generate_v4()")
    )
    log_book_attachment = db.Column(db.String(255), nullable=False)

    __mapper_args__ = {
        'polymorphic_identity': ProductTypes.MOTOR_COMMERCIAL,
    }

    def __repr__(self):
        return '<MotorCommercialPolicy %r>' % (self.id)


class MedicalInpatientPolicy(Policy, MedicalMixin):

    __tablename__ = 'medical_inpatient_policies'

    id = db.Column(
        UUID(as_uuid=True),
        db.ForeignKey('policies.id'),
        primary_key=True,
        server_default=text("uuid_generate_v4()")
    )

    __mapper_args__ = {
        'polymorphic_identity': ProductTypes.MEDICAL_INPATIENT,
    }

    def __repr__(self):
        return '<MedicalInpatientPolicy %r>' % (self.id)


class MedicalOutpatientPolicy(Policy, MedicalMixin):

    __tablename__ = 'medical_outpatient_policies'

    id = db.Column(
        UUID(as_uuid=True),
        db.ForeignKey('policies.id'),
        primary_key=True,
        server_default=text("uuid_generate_v4()")
    )

    __mapper_args__ = {
        'polymorphic_identity': ProductTypes.MEDICAL_OUTPATIENT,
    }

    def __repr__(self):
        return '<MedicalOutpatientPolicy %r>' % (self.id)
