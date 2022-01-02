from flask import Flask
from flask_migrate import Migrate
from flask_restful import Api
from flask_sqlalchemy import SQLAlchemy

from app.api import create_api
from app.config import SWAGGER_BLUEPRINT, SWAGGER_URL, AppConfig
from app.routes import create_routes


def create_app():
    app = Flask(__name__)
    app.config.from_object(AppConfig)
    db = SQLAlchemy(app)
    migrate = Migrate(app, db)
    api = Api(app)

    app.register_blueprint(SWAGGER_BLUEPRINT, url_prefix=SWAGGER_URL)

    return app


def main():
    app = create_app()
    api = create_api(app)
    create_routes(api)
    app.run()


if __name__ == "__main__":
    main()
