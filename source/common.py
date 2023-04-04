from typing import Optional

from .models import User


def retrieve_user_from_token(token) -> User:
    user_id: str = User.decode_auth_token(auth_token=token)
    user: Optional[User] = User.query.get(user_id)
    return user
