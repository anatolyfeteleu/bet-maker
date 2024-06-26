from datetime import timezone
from pathlib import Path

from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    HOST_PROTOCOL: str = "http"
    HOST_ADDR: str = "0.0.0.0"
    HOST_PORT: int = 8000

    DB_NAME: str
    DB_USERNAME: str
    DB_HOSTNAME: str
    DB_PORT: str
    DB_PASSWORD: str


BASE_DIR = Path()
SETTINGS = Settings(_env_file=".env", _env_file_encoding="utf-8")
TZ = timezone.utc
