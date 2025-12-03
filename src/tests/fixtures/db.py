import pytest

from config.settings import Settings
from di import resolve


@pytest.fixture(autouse=True)
def settings() -> Settings:
    """Configure settings for testing."""
    settings = resolve(Settings)
    settings.DB_PATH = ':memory:'
    settings.LOG_NAME = ''
    return settings
