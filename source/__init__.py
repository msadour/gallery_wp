from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

db: SQLAlchemy = SQLAlchemy()
migrate: Migrate = Migrate()
API_key: str = "23c9841cf0d64d3f8b2625285e3cc497"


def init_app() -> Flask:
    app: Flask = Flask(__name__)
    app.config["DEBUG"] = True
    app.config[
        "SQLALCHEMY_DATABASE_URI"
    ] = "postgresql://postgres:qwertz@localhost:5433/gallery_wp"
    app.secret_key = API_key

    from .models import User

    db.init_app(app)
    migrate.init_app(app, db)

    from .gallery.views import bp_gallery
    from .user.views import bp_user

    app.register_blueprint(bp_gallery)
    app.register_blueprint(bp_user)

    return app
