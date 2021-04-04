from os import environ

wsgi_app = 'wsgi:app'
bind = '%s:%s' % (
    environ.get("APP_HOST"),
    environ.get("APP_PORT")
)
workers = environ.get("WORKERS")
threads = environ.get("THREADS")
max_requests = environ.get("MAX_REQUESTS")
loglevel = environ.get("LOG_LEVEL")
accesslog =  "./logs/gunicorn-access.log"
errorlog = "./logs/gunicorn-error.log"
capture_output= environ.get("CAPTURE_OUTPUT")
timeout = environ.get("TIMEOUT")
reload = environ.get("RELOAD")