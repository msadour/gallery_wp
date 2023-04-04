from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

from .config import Config

db: SQLAlchemy = SQLAlchemy()
migrate: Migrate = Migrate()
API_key: str = Config.API_KEY


def init_app() -> Flask:
    app: Flask = Flask(__name__)
    app.config["DEBUG"] = Config.DEBUG
    db_uri: str = f"postgresql://{Config.DB_USER}:{Config.DB_PASSWORD}@{Config.DB_HOST}:{Config.DB_PORT}/{Config.DB_NAME}"
    app.config["SQLALCHEMY_DATABASE_URI"] = db_uri
    app.secret_key = API_key

    from .models import User

    db.init_app(app)
    migrate.init_app(app, db)

    from .gallery.views import bp_gallery
    from .user.views import bp_user

    app.register_blueprint(bp_gallery)
    app.register_blueprint(bp_user)

    return app
