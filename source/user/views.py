from flask import session, request, jsonify, Blueprint

from .utils import (
    get_user_logged,
    perform_signup,
    get_token_from_request,
    retrieve_user_from_token,
    perform_delete,
)


bp_user = Blueprint("bp_user", __name__)


@bp_user.route("/login", methods=("POST",))
def login():
    username: str = request.json["username"]
    password: str = request.json["password"]
    user = get_user_logged(username=username, password=password)
    token = user.encode_auth_token()
    return jsonify(token=token), 200


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

    user = get_user_logged(username=username, password=password)
    token = user.encode_auth_token()

    return jsonify(token=token), 201


@bp_user.route("/delete_account", methods=("POST",))
def delete_account():
    token = get_token_from_request(request=request)
    user = retrieve_user_from_token(token=token)
    perform_delete(user)
    return jsonify(message="User deleted"), 204
