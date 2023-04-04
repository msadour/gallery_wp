import os

from dotenv import load_dotenv


env_path = os.path.dirname(os.path.abspath(__file__)) + "/.env"
load_dotenv(env_path)


class Config:
    DEBUG = os.environ.get("DEBUG")
    DB_USER = os.environ.get("DB_USER")
    DB_PASSWORD = os.environ.get("DB_PASSWORD")
    DB_HOST = os.environ.get("DB_HOST")
    DB_PORT = os.environ.get("DB_PORT")
    DB_NAME = os.environ.get("DB_NAME")
    API_KEY = os.environ.get("API_KEY")
