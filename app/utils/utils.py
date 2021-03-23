import jwt
from os import environ
from functools import wraps
from flask import session, redirect, url_for

def decode_token(bearer_token):
    token = bearer_token.split(" ")[1]
    return jwt.decode(token, environ.get('JWT_SECRET_KEY'), algorithms=['HS256'])


def login_required(view):
    @wraps(view)
    def wrapped_view(**kwargs):
        if 'authorization' not in session:
            return redirect(url_for('auth.login'))

        return view(**kwargs)

    return wrapped_view
