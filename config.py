# Statement for enabling the development environment
DEBUG = True

# Define the application directory
import os
BASE_DIR = os.path.abspath(os.path.dirname(__file__))  

# Define the database - we are working with
# SQLite for this example
SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(BASE_DIR, 'app.db')
SQLALCHEMY_TRACK_MODIFICATIONS = False
DATABASE_CONNECT_OPTIONS = {}

# Application threads. A common general assumption is
# using 2 per available processor cores - to handle
# incoming requests using one and performing background
# operations using the other.
THREADS_PER_PAGE = 2

# Enable protection agains *Cross-site Request Forgery (CSRF)*
CSRF_ENABLED     = True

# Use a secure, unique and absolutely secret key for
# signing the data. 
CSRF_SESSION_KEY = "secret"

# Secret key for signing cookies
SECRET_KEY = "secret"







# argument_list = sys.argv

# if len(argument_list) == 1:
#     if backend_api.config['DB_STATE'] == "DEV":
#         print("running development persistance in sqlite")
#         base_dir = os.path.abspath(os.path.dirname(__file__))
#         backend_api.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///"+os.path.join(base_dir, 'data.sqlite')
#         backend_api.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
#     else:
#         print("running production persistance in mysql")
#         backend_api.config['SQLALCHEMY_DATABASE_URI'] = "mysql://root:rootpassword@iphonecity_db/test_db"
#         backend_api.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
# else:
#     persistance_arg = argument_list[1]
#     print("running development persistance in sqlite")
#     base_dir = os.path.abspath(os.path.dirname(__file__))
#     backend_api.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///"+os.path.join(base_dir, 'data.sqlite')
#     backend_api.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False