from os import environ
from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_mail import Mail
from settings.config import AppConfig
from settings.emails import mail_settings

db = SQLAlchemy()
mail = Mail()


def create_app():
    app = Flask(__name__)

    # Set app Configuration
    app.config.from_object(AppConfig)
    app.config.update(mail_settings)

    # Initializations
    db.init_app(app)
    mail.init_app(app)

    Migrate(app, db)

    # Register Blueprints
    from .admin import admin as admin_blueprint
    app.register_blueprint(admin_blueprint)

    from .auth import auth as auth_blueprint
    app.register_blueprint(auth_blueprint)

    from .home import home as home_blueprint
    app.register_blueprint(home_blueprint)

    from .customer import customer as customer_blueprint
    app.register_blueprint(customer_blueprint)

    return app
