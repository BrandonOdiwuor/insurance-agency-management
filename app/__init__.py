from flask import Flask, render_template

from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

# Configurations
app.config.from_object('config')

JWT_SECRET_KEY = "\x95\xa7\xee?\xfb\xaa\x07\n(e\xb8\x03\xab"
JWT_TOKEN_LIFE_IN_SECONDS = 2880

db = SQLAlchemy(app)

# Sample HTTP error handling
@app.errorhandler(404)
def not_found(error):
    return render_template('404.html'), 404

from app.views import mod_app as app_module

app.register_blueprint(app_module)

db.create_all()