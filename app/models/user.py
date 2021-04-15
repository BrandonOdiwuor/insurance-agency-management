from os import environ
from datetime import datetime, timedelta
from werkzeug.security import generate_password_hash, check_password_hash
import jwt
from app.models import Base
from app import db
from app.utils.enums import CustomerStatus


class User(Base):

    __tablename__ = 'users'

    f_name = db.Column(db.String(20), nullable=False)
    l_name = db.Column(db.String(20),  nullable=False)
    email = db.Column(db.String(100), unique=True, nullable=False)
    password_hash = db.Column(db.String(200), nullable=False)
    user_type = db.Column(db.String(20))
    phone = db.Column(db.String(9), unique=True, nullable=False)

    def token(self):
        generated = datetime.now()
        expiry = datetime.now() + timedelta(seconds=int(environ.get('JWT_TOKEN_LIFE_IN_SECONDS')))

        token = jwt.encode(
            {
                "uid": str(self.id),
                "exp": int(expiry.strftime("%s")),
                "iat": int(generated.strftime("%s")),
            },
            environ.get('JWT_SECRET_KEY'),
            algorithm="HS256",
        )

        return token

    @property
    def password(self):
        """
        Prevent pasword from being accessed
        """
        raise AttributeError('password is not a readable attribute.')

    @password.setter
    def password(self, password):
        """
        Set password to a hashed password
        """
        self.password_hash = generate_password_hash(password)

    def verify_password(self, password):
        """
        Check if hashed password matches actual password
        """
        return check_password_hash(self.password_hash, password)

    def __repr__(self):
        return '<User %r>' % (self.email)
