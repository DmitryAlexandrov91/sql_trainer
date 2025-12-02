import os
from pydantic_settings import BaseSettings, SettingsConfigDict
from pathlib import Path


class Settings(BaseSettings):
    """Base project settings."""

    base_dir: Path = Path(__file__).resolve().parent.parent
    db_name: str = 'training_db.sqlite3'
    db_path: str = os.path.join(base_dir, db_name)

    model_config = SettingsConfigDict(env_file='.env')
