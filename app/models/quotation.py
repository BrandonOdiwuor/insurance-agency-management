from app.models import Base
from app import db


class Quotation(Base):

    __tablename__ = 'quotations'

    client_email = db.Column(db.String(100), unique=True, nullable=False)
    client_phone = db.Column(db.String(9), unique=True, nullable=False)
    item_id = db.Column(db.Integer)

    def __repr__(self):
        return '<Quotation %r>' % (self.id)
