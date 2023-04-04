from typing import Optional

from ..exceptions import (
    UsernameNotExistException,
    WrongPasswordException,
    UsernameAlreadyExistException,
)
from ..models import User, db
from ..common import retrieve_user_from_token


def perform_login(username: str, password: str) -> str:
    user: Optional[User] = User.query.filter(User.username == username).first()

    if user is None:
        raise UsernameNotExistException()

    if not user.verify_password(password):
        raise WrongPasswordException()

    token: str = user.encode_auth_token()

    return token


def perform_signup(
    username: str, password: str, first_name: str, last_name: str
) -> None:
    user_with_username: User = User.query.filter(User.username == username).first()

    if user_with_username:
        raise UsernameAlreadyExistException()

    new_user: User = User(
        username=username, password=password, first_name=first_name, last_name=last_name
    )

    db.session.add(new_user)
    db.session.commit()


def perform_delete(token: str):
    user = retrieve_user_from_token(token=token)
    db.session.delete(user)
    db.session.commit()
