import os
from uuid import UUID, uuid4

from PIL import Image
from werkzeug.datastructures import FileStorage
from flask import Request

from ..models import User
from ..common import retrieve_user_from_token


def get_token_from_request(request: Request) -> str:
    auth_header: str = request.headers.get("Authorization")
    if not auth_header:
        raise Exception("Token is mandatory.")

    auth_token: str = auth_header.split(" ")[1]
    return auth_token


def perform_upload_image(token: str, file: FileStorage) -> None:
    user: User = retrieve_user_from_token(token=token)
    current_path: str = os.path.dirname(os.path.abspath(__file__))
    user_gallery_path: str = f"{current_path}/gallery/{user.username}"
    if not os.path.exists(user_gallery_path):
        os.makedirs(user_gallery_path)

    unique_image_name: UUID = uuid4()
    type_image: str = file.mimetype.split("/")[1]
    file.save(f"{user_gallery_path}/{unique_image_name}.{type_image}")


def get_image_encoded(image_path: str) -> bytes:
    pil_img: Image = Image.open(f"{image_path}")
    pil_img_decoded: bytes = pil_img.tobytes("xbm", "rgb").decode()
    return pil_img_decoded


def get_user_images(user_gallery_path: str) -> list:
    all_images_name: list = os.listdir(user_gallery_path)
    all_images: list = [
        get_image_encoded(f"{user_gallery_path}/{file_name}")
        for file_name in all_images_name
    ]
    return all_images


def perform_get_images(token: str) -> list:
    user: User = retrieve_user_from_token(token=token)
    current_path: str = os.path.dirname(os.path.abspath(__file__))
    user_gallery_path: str = f"{current_path}/images_users/{user.username}"
    encoded_images: list = get_user_images(user_gallery_path=user_gallery_path)
    return encoded_images


def perform_get_image(token: str, image_id: str, extension: str) -> bytes:
    user: User = retrieve_user_from_token(token=token)
    current_path: str = os.path.dirname(os.path.abspath(__file__))
    image_path: str = (
        f"{current_path}/images_users/{user.username}/{image_id}.{extension}"
    )
    image: bytes = get_image_encoded(image_path=image_path)
    return image
