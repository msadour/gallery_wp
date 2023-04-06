from flask import request, jsonify, Blueprint
from werkzeug.datastructures import FileStorage

from .utils import ImageManager

from ..common import get_token_from_request


bp_gallery = Blueprint("bp_gallery", __name__)


@bp_gallery.route("/upload_image", methods=("POST",))
def upload_image():
    token: str = get_token_from_request(request=request)
    file: FileStorage = request.files["file"]
    ImageManager(token=token).perform_upload_image(file=file)
    return jsonify(message="Image uploaded"), 201


@bp_gallery.route("/get_images", methods=("GET",))
def get_images():
    token: str = get_token_from_request(request=request)
    images: list = ImageManager(token=token).perform_get_images()
    return jsonify(images=images), 200


@bp_gallery.route("/get_image/<image_id>", methods=("GET",))
def get_single_image(image_id):
    token: str = get_token_from_request(request=request)
    image: str = ImageManager(token=token).perform_get_image(image_id=image_id)
    return jsonify(image=image), 200
