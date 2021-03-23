from os import environ, path
from dotenv import load_dotenv
from app import create_app

BASE_DIR = path.dirname(path.dirname(path.abspath(__file__)))

# Load the environmental variables
load_dotenv(dotenv_path='.env')

config_name = environ.get('FLASK_CONFIG')
app = create_app(config_name)

if __name__ == '__main__':
    app.run(
       host=environ.get('HOST'),
       port=environ.get('PORT')
    )
