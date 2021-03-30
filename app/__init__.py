from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from settings import app_config
from os import environ

db = SQLAlchemy()


def create_app(config_name):
    app = Flask(__name__)
    db.init_app(app)

    # Select appropriate Configuration
    app.config.from_object(app_config[config_name])

    _ = Migrate(app, db)

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
