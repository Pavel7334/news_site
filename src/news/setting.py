from pydantic_settings import BaseSettings
from dotenv import load_dotenv

import os

load_dotenv()


class Settings(BaseSettings):
    server_host: str = '127.0.0.1'
    server_port: int = 8000
    db_host: str = os.environ.get("db_host")
    db_port: str = os.environ.get("db_port")
    db_name: str = os.environ.get("db_name")
    db_user: str = os.environ.get("db_user")
    db_pass: str = os.environ.get("db_pass")


settings = Settings(
    _env_file='.env',
    _env_file_encoding='utf-8',
)
