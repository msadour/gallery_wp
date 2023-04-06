import os
from uuid import UUID, uuid4

from werkzeug.datastructures import FileStorage

from ..common import retrieve_user_from_token
from ..exceptions import WrongFormatImageException


class ImageManager:
    def __init__(self, token: str):
        self.user = retrieve_user_from_token(token=token)
        self.current_path = os.path.dirname(os.path.abspath(__file__))
        self.supported_format = ["jpg", "jpeg", "png", "webp"]

    def perform_upload_image(self, file: FileStorage) -> None:
        user_gallery_path: str = (
            f"{self.current_path}/images_users/{self.user.username}"
        )
        if not os.path.exists(user_gallery_path):
            os.makedirs(user_gallery_path)

        unique_image_name: UUID = uuid4()
        type_image: str = file.mimetype.split("/")[1]
        if type_image not in self.supported_format:
            raise WrongFormatImageException()
        file.save(f"{user_gallery_path}/{unique_image_name}.{type_image}")

    @staticmethod
    def get_user_images(user_gallery_path: str) -> list:
        all_images_name: list = os.listdir(user_gallery_path)
        all_images: list = [
            f"{user_gallery_path}/{file_name}" for file_name in all_images_name
        ]
        return all_images

    def perform_get_images(self) -> list:
        user_gallery_path: str = (
            f"{self.current_path}/images_users/{self.user.username}"
        )
        encoded_images: list = self.get_user_images(user_gallery_path=user_gallery_path)
        return encoded_images

    def perform_get_image(self, image_id: str) -> str:
        images_user_path: str = f"{self.current_path}/images_users/{self.user.username}"
        image: str = [
            image for image in os.listdir(images_user_path) if image_id in image
        ][0]
        return image
