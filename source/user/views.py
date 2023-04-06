from flask import session, request, jsonify, Blueprint

from .utils import (
    perform_login,
    perform_signup,
    perform_delete,
)
from ..common import get_token_from_request


bp_user = Blueprint("bp_user", __name__)


@bp_user.route("/login", methods=("POST",))
def login():
    username: str = request.json["username"]
    password: str = request.json["password"]
    data: dict = perform_login(username=username, password=password)
    return jsonify(**data), 200


@bp_user.route("/logout", methods=("POST",))
def logout():
    session.clear()
    return 204


@bp_user.route("/signup", methods=("POST",))
def signup():
    username: str = request.json["username"]
    password: str = request.json["password"]
    first_name: str = request.json["first_name"]
    last_name: str = request.json["last_name"]

    perform_signup(
        username=username, password=password, first_name=first_name, last_name=last_name
    )

    data: dict = perform_login(username=username, password=password)

    return jsonify(**data), 201


@bp_user.route("/delete_account", methods=("DELETE",))
def delete_account():
    token: str = get_token_from_request(request=request)
    perform_delete(token=token)
    return jsonify(message="User deleted"), 204
