from app.config.config import Config
from app.flask_application import FlaskApplication

app = FlaskApplication.create_app(Config)
