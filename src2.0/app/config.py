import pathlib

from flask_swagger_ui import get_swaggerui_blueprint

BASE_DIR = pathlib.Path(__file__).resolve().parent

SWAGGER_URL = '/swagger/'
SWAGGER_BLUEPRINT = get_swaggerui_blueprint(
    SWAGGER_URL,
    '/static/swagger.json',
    config={
        'app_name': 'flask_test'
    }
)




class AppConfig:
    SQLALCHEMY_DATABASE_URI = 'sqlite:///' + str(BASE_DIR) + "data/db.sqlite3"
    SQLALCHEMY_TRACK_MODIFICATIONS = False
