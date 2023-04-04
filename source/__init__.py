import flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

db = SQLAlchemy()
migrate = Migrate()
API_key = "23c9841cf0d64d3f8b2625285e3cc497"


def init_app():
    app = flask.Flask(__name__)
    app.config["DEBUG"] = True
    app.config['SQLALCHEMY_DATABASE_URI'] = "postgresql://postgres:qwertz@localhost:5433/gallery_wp"
    app.secret_key = API_key

    from .models import User

    db.init_app(app)
    migrate.init_app(app, db)

    from .routes import main as main_blueprint
    app.register_blueprint(main_blueprint)

    return app
