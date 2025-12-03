import os
from pathlib import Path

from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    """Base project settings."""

    BASE_DIR: Path = Path(__file__).resolve().parent.parent
    DB_NAME: str = 'db.sqlite3'
    DB_PATH: str = os.path.join(BASE_DIR, DB_NAME)

    FORMAT_LOG: str = '{time:YYYY-MM-DD at HH:mm:ss} | {level} | {message}'
    LOG_ROTATION: str = '10 MB'
    LOG_NAME: str = 'log.txt'

    model_config = SettingsConfigDict(
        env_file='.env', env_file_encoding='utf-8'
    )
