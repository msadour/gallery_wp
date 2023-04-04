from flask import session, request, jsonify, Blueprint

from .utils import get_user_logged, perform_signup, get_token_from_request, retrieve_user_from_token, perform_delete


main = Blueprint('main', __name__)


@main.route('/login', methods=('POST',))
def login():
    username: str = request.json["username"]
    password: str = request.json["password"]
    user = get_user_logged(username=username, password=password)
    return jsonify(token=user.encode_auth_token()), 200


@main.route('/logout', methods=('POST',))
def logout():
    session.clear()
    return 204


@main.route('/signup', methods=('POST',))
def signup():
    username: str = request.json["username"]
    password: str = request.json["password"]
    first_name: str = request.json["first_name"]
    last_name: str = request.json["last_name"]

    perform_signup(username=username, password=password, first_name=first_name, last_name=last_name)

    user = get_user_logged(username=username, password=password)
    session['username'] = user.username

    return jsonify(token=user.encode_auth_token()), 201


@main.route('/delete_account', methods=('POST',))
def delete_account():
    token = get_token_from_request(request=request)
    user = retrieve_user_from_token(token=token)
    perform_delete(user)
    return jsonify(message="User deleted."), 204
