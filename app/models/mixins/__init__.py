from app import db
from app.utils.enums import PaymentPlans, ProductTypes


class BaseProductMixin(object):
    policy_start_date = db.Column(
        db.DateTime,  default=db.func.current_timestamp()
    )
    sum_insured = db.Column(db.Float, nullable=False)
    payment_plan = db.Column(db.Enum(PaymentPlans), nullable=False)
    premium = db.Column(db.Float, nullable=False)
