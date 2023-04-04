from . import init_app, db
from .models import User

myapp = init_app()


@myapp.shell_context_processor
def make_shell_context():
    return dict(db=db, User=User)
