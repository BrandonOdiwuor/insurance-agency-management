from app.models.mixins import BaseProductMixin
from app import db
from app.utils.enums import MotorPolicyTypes, PolicyStatus


class MotorRiskDetailMixin(object):
    motor_model = db.Column(db.String(255), nullable=False)
    motor_make = db.Column(db.String(255), nullable=False)
    motor_year_of_manufacture = db.Column(
        db.Integer, default=2000, nullable=False
    )
    motor_seating_capacity = db.Column(db.Integer, default=1)
    motor_registration_number = db.Column(db.String(25), unique=True)
    motor_engine_number = db.Column(db.String(255))
    motor_engine_cc = db.Column(db.Integer)


class MotorMixin(BaseProductMixin, MotorRiskDetailMixin):
    motor_use = db.Column(db.String(255), nullable=False)
    motor_policy_type = db.Column(db.Enum(MotorPolicyTypes), nullable=False)
    recent_profesional_evaluation = db.Column(
        db.Boolean, nullable=False, default=False
    )
