from os import environ, path
from dotenv import load_dotenv


class Config:
    basedir = path.abspath(path.dirname(__file__))
    load_dotenv(path.join(basedir, '.env'))
    """Set Flask config variables."""

    FLASK_ENV = environ.get('FLASK_ENV')
    # TESTING = True
    SECRET_KEY = environ.get('SECRET_KEY')
