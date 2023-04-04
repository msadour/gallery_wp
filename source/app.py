# import flask
# from flask_sqlalchemy import SQLAlchemy
# from flask_restful import Api
# from flask_migrate import Migrate
#
# from app.endpoints.bp import bp_auth
#
# app = flask.Flask(__name__)
# app.config["DEBUG"] = True
# app.config['SQLALCHEMY_DATABASE_URI'] = "postgresql://postgres:qwertz@localhost:5433/gallery_wp"
#
# api = Api(app)
# app.register_blueprint(bp_auth, url_prefix='/auth')
#
# db = SQLAlchemy(app)
# migrate = Migrate(app, db)
#
# import import_models
#
# if __name__ == '__main__':
#     app.run(debug=True)


from . import init_app, db
from .models import User, Image

myapp = init_app()


@myapp.shell_context_processor
def make_shell_context():
    return dict(db=db, Tutor=User, Student=Image)
