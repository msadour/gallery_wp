from flask import request, jsonify, Blueprint
from werkzeug.datastructures import FileStorage

from .utils import (
    get_token_from_request,
    perform_upload_image,
    perform_get_images,
    perform_get_image,
)

from ..common import retrieve_user_from_token


bp_gallery = Blueprint("bp_gallery", __name__)


@bp_gallery.route("/upload_image", methods=("POST",))
def upload_image():
    token: str = get_token_from_request(request=request)
    file: FileStorage = request.files["image"]
    perform_upload_image(token=token, file=file)
    return jsonify(message="Image uploaded"), 201


@bp_gallery.route("/get_images", methods=("GET",))
def get_images():
    token: str = get_token_from_request(request=request)
    images: list = perform_get_images(token=token)
    return jsonify(images=images), 200


@bp_gallery.route("/get_image/<image_id>", methods=("GET",))
def get_single_image(image_id):
    token: str = get_token_from_request(request=request)
    extension: str = request.args.get("extension")
    image: bytes = perform_get_image(
        token=token, image_id=image_id, extension=extension
    )
    return jsonify(image=image), 200
