from app import db
from app.utils.enums import PaymentPlans, ProductTypes, PolicyStatus


class BaseProductMixin(object):
    policy_start_date = db.Column(
        db.DateTime,  default=db.func.current_timestamp()
    )
    sum_insured = db.Column(db.Float, nullable=False)
    payment_plan = db.Column(db.Enum(PaymentPlans), nullable=False)
    premium = db.Column(db.Float, nullable=False)


class BasePolicyMixin(object):
    policy_status = db.Column(db.Enum(PolicyStatus), nullable=False)
    policy_expiry_date = db.Column(
        db.DateTime,  default=db.func.current_timestamp()
    )
    policy_number = db.Column(db.String(255), nullable=False)
    policy_underwriter = db.Column(db.String(255), nullable=False)
