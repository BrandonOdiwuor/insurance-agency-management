from app import db
from app.models.mixins import BaseProductMixin


class MedicalMixin(BaseProductMixin):
    pre_existing_condition = db.Column(
        db.Boolean, nullable=False, default=False
    )
    date_of_birth = db.Column(
        db.DateTime,  default=db.func.current_timestamp()
    )
