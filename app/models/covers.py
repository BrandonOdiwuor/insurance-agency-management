from app.models import Base
from app import db


class Cover(Base):

    __tablename__ = 'covers'

    customer_id = db.Column(db.Integer)

    def __repr__(self):
        return '<Cover %r>' % (self.id)
