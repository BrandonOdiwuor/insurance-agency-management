from os import path, environ

class Config(object):
    """
    Common configurations
    """
    
    # Statement for enabling the development environment'
    DEBUG = environ.get('DEBUG', False)
    FLASK_ENV=environ.get('FLASK_CONFIG')
    ENV=environ.get('FLASK_CONFIG')

    # Application's directory
    BASE_DIR = path.abspath(path.dirname(__file__))

    # Enable protection agains *Cross-site Request Forgery (CSRF)*
    CSRF_ENABLED = True

    # Use a secure, unique and absolutely secret key for
    # signing the data.
    CSRF_SESSION_KEY = environ.get('CSRF_SESSION_KEY', False)

    # Secret key for signing cookies
    SECRET_KEY = environ.get('SECRET_KEY', False)

    # JWT secret key
    JWT_SECRET_KEY = environ.get('JWT_SECRET_KEY')
    JWT_TOKEN_LIFE_IN_SECONDS = int(environ.get('JWT_TOKEN_LIFE_IN_SECONDS', 2880))

    # Don't track object modifications
    SQLALCHEMY_TRACK_MODIFICATIONS = False

class DevelopmentConfig(Config):
    """
    Development configurations
    """
    # Enable the development environment
    DEBUG = True

    # Log SQL statements
    SQLALCHEMY_ECHO = True

    # Development database
    SQLALCHEMY_DATABASE_URI = 'sqlite:///' + path.join(Config.BASE_DIR, 'app.db')


class ProductionConfig(Config):
    """
    Production configurations
    """
     # Production database
    SQLALCHEMY_DATABASE_URI = environ.get('DATABASE')

app_config = {
    'development': DevelopmentConfig,
    'production': ProductionConfig
}
