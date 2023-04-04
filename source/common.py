from typing import Optional

from flask import Request

from .models import User


def retrieve_user_from_token(token: str) -> User:
    user_id: str = User.decode_auth_token(auth_token=token)
    user: Optional[User] = User.query.get(user_id)
    if user is None:
        raise Exception("Wrong token")
    return user


def get_token_from_request(request: Request) -> str:
    auth_header: str = request.headers.get("Authorization")
    if not auth_header:
        raise Exception("Token is mandatory")

    auth_token: str = auth_header.split(" ")[1]
    return auth_token
