from flask import session, request, jsonify, Blueprint

from .utils import (
    get_token_from_request,
    retrieve_user_from_token,
    perform_upload_image,
    perform_get_images,
    perform_get_image,
)


bp_gallery = Blueprint("bp_gallery", __name__)


@bp_gallery.route("/upload_image", methods=("POST",))
def upload_image():
    token = get_token_from_request(request=request)
    user = retrieve_user_from_token(token=token)
    file = request.files["image"]
    perform_upload_image(user, file=file)
    return jsonify(message="Image uploaded"), 201


@bp_gallery.route("/get_images", methods=("GET",))
def get_images():
    token = get_token_from_request(request=request)
    user = retrieve_user_from_token(token=token)
    images = perform_get_images(user)
    return jsonify(images=images), 200


@bp_gallery.route("/get_image/<image_id>", methods=("GET",))
def get_single_image(image_id):
    token = get_token_from_request(request=request)
    user = retrieve_user_from_token(token=token)
    extension = request.args.get("extension")
    image = perform_get_image(user=user, image_id=image_id, extension=extension)
    return jsonify(image=image), 200
