from sqlalchemy.dialects.postgresql import UUID
from app.models import Base
from app.models.mixins.motor_mixins import MotorPolicyMixin
from app import db


class PrivateMotorPolicy(Base, MotorPolicyMixin):

    __tablename__ = 'private_motor_policy'

    customer_id = UUID(as_uuid=True),
        db.ForeignKey('customers.id'),
        nullable = False
    )

    def __repr__(self):
        return '<MotorPrivatePolicy %r>' % (self.id)
