import os
import uuid
from typing import Optional

from .exceptions import UsernameException, WrongPassword
from .models import User, db


def get_user_logged(username, password) -> User:
    user: Optional[User] = User.query.filter(User.username == username).first()

    if user is None:
        raise UsernameException()

    if not user.verify_password(password):
        raise WrongPassword()

    return user


def perform_signup(username: str, password: str, first_name: str, last_name: str) -> User:
    user_with_username: User = User.query.filter(User.username == username).first()

    if user_with_username:
        raise Exception("This username exist.")

    new_user: User = User(
        username=username,
        password=password,
        first_name=first_name,
        last_name=last_name
    )

    db.session.add(new_user)
    db.session.commit()

    return new_user


def retrieve_user_from_token(token) -> User:
    user_id: str = User.decode_auth_token(auth_token=token)
    user: Optional[User] = User.query.get(user_id)
    return user


def get_token_from_request(request) -> str:
    auth_header = request.headers.get('Authorization')
    if not auth_header:
        raise Exception("Token is mandatory.")

    auth_token = auth_header.split(" ")[1]
    return auth_token


def perform_delete(user: User):
    db.session.delete(user)
    db.session.commit()


def perform_upload_image(user: User, file=None):
    current_path = os.path.dirname(os.path.abspath(__file__))
    user_gallery_path = f"{current_path}/gallery/{user.username}"
    if not os.path.exists(user_gallery_path):
        os.makedirs(user_gallery_path)

    unique_image_name = uuid.uuid4()
    type_image = file.mimetype.split("/")[1]
    file.save(f"{user_gallery_path}/{unique_image_name}.{type_image}")


def perform_get_images(user):
    pass
