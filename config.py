import os
import pathlib

BASE_DIR = pathlib.Path(__file__).parent


class Config:
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL').replace("://", "ql://", 1) or 'sqlite:///' + str(BASE_DIR / "data" / "db.sqlite3")


    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SECRET_KEY = 'you-will-newer-know'
