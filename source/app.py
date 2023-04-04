from flask import Flask

from . import init_app, db
from .models import User

myapp: Flask = init_app()


@myapp.shell_context_processor
def make_shell_context() -> dict:
    return dict(db=db, User=User)
