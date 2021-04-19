import jwt
from secrets import token_urlsafe
from os import environ, path
from functools import wraps
from flask import session, redirect, url_for
from werkzeug.utils import secure_filename


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


ALLOWED_EXTENSIONS = {'pdf', 'png', 'jpg', 'jpeg'}


def save_file(file):
    if '.' in file.filename:
        file_ext = file.filename.rsplit('.', 1)[1].lower()
        if file_ext in ALLOWED_EXTENSIONS:
            filename = secure_filename(token_urlsafe(24) + '.' + file_ext)
            file.save(path.join(environ.get('UPLOAD_FOLDER'), filename))
            return filename
    return None


def get_customer_form_payload(form):
    return {
        'first_name': form.first_name.data,
        'last_name': form.last_name.data,
        'national_id_number': form.national_id_number.data,
        'primary_phone_number': form.primary_phone_number.data,
        'primary_email': form.primary_email.data,
        'password': 'pass@123',  # To DO: -FIX autogenerate password
        'physical_address': form.physical_address.data,
        'city': form.city.data,
        'county': form.county.data,
        'postal_address': form.postal_address.data,
        'postal_code': form.postal_code.data,
        'gender': form.gender.data,
        'birth_date': form.birth_date.data,
        'kra_pin': form.kra_pin.data
    }