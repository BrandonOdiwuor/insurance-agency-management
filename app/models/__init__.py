from os import environ
from datetime import datetime, timedelta
from werkzeug.security import generate_password_hash, check_password_hash
import jwt
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy import text
from app import db
from app.utils.enums import CustomerStatus, InvoiceStatus, PaymentModes


class Base(db.Model):
    __abstract__ = True
    id = db.Column(
        UUID(as_uuid=True), 
        primary_key=True, 
        server_default=text("uuid_generate_v4()")
    )
    created_at = db.Column(db.DateTime,  default=db.func.current_timestamp())
    updated_at = db.Column(db.DateTime,  default=db.func.current_timestamp(),
                           onupdate=db.func.current_timestamp())
