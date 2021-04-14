from app.models import Base
from app import db


class SaleItem(Base):

    __tablename__ = 'sale_items'

    name = db.Column(db.String(20))
    category = db.Column(db.String(20))
    price = db.Column(db.Float)
    item_quote_procedure_json = db.Column(db.JSON)
    details_json = db.Column(db.JSON)

    def __repr__(self):
        return '<Product %r>' % (self.name)
