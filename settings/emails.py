
from os import environ

mail_settings = {
    "MAIL_SERVER": environ['MAIL_SERVER'],
    "MAIL_PORT": environ['MAIL_PORT'],
    #"MAIL_USE_TLS": environ['MAIL_USE_TLS'],
    "MAIL_USE_SSL": environ['MAIL_USE_SSL'],
    "MAIL_USERNAME": environ['EMAIL_USER'],
    "MAIL_PASSWORD": environ['EMAIL_PASSWORD'],
    "MAIL_DEFAULT_SENDER": environ['EMAIL_USER']
}