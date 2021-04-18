from app.models import Base
from app import db


class SaleItem(Base):

    __tablename__ = 'sale_items'

    name = db.Column(db.String(255), nullable=False)
    category = db.Column(db.String(255), nullable=False)
    price = db.Column(db.Float)
    details_json = db.Column(db.JSON)

    def __repr__(self):
        return '<Product %r>' % (self.name)
