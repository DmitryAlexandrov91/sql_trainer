import os
from pathlib import Path

from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    """Base project settings."""

    base_dir: Path = Path(__file__).resolve().parent.parent
    db_name: str = 'db.sqlite3'
    db_path: str = os.path.join(base_dir, db_name)

    FORMAT_LOG: str = "{time:YYYY-MM-DD at HH:mm:ss} | {level} | {message}"
    LOG_ROTATION: str = "10 MB"
    

    model_config = SettingsConfigDict(env_file='.env')
