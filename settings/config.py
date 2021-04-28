from os import path, environ

class AppConfig(object):
    """
    Application configurations
    """

    # Application's directory
    BASE_DIR = path.abspath(path.dirname(__file__))

    # Secret key for signing cookies
    SECRET_KEY = environ.get('SECRET_KEY', False)

    # JWT secret key
    JWT_SECRET_KEY = environ.get('JWT_SECRET_KEY')
    JWT_TOKEN_LIFE_IN_SECONDS = int(
        environ.get('JWT_TOKEN_LIFE_IN_SECONDS', 2880))

    SQLALCHEMY_DATABASE_URI = "postgresql+psycopg2://%s:%s@%s:%s/%s" % (
        environ.get('DB_USER'),
        environ.get('DB_PASSWORD'),
        environ.get('DB_HOST'),
        environ.get('DB_PORT'),
        environ.get('DB_NAME')
    )    

    # Log SQL statements
    # SQLALCHEMY_ECHO = environ.get('SQLALCHEMY_ECHO', False)

    # Don't track object modifications
    SQLALCHEMY_TRACK_MODIFICATIONS = environ.get(
        'SQLALCHEMY_TRACK_MODIFICATIONS', False
    )
