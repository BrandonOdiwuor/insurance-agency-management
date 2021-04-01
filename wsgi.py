from os import environ, path
from app import create_app

BASE_DIR = path.dirname(path.dirname(path.abspath(__file__)))

app = create_app()

if __name__ == '__main__':
    app.run(
       host=environ.get('APP_HOST'),
       port=environ.get('APP_PORT')
    )
