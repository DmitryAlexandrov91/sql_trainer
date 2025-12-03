import pytest

from config.settings import Settings
from di import resolve


@pytest.fixture(autouse=True)
def settings() -> Settings:
    """Configure test settings."""
    settings = resolve(Settings)
    settings.DB_PATH = ':memory:'
    return settings
