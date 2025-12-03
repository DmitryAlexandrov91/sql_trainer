from config.settings import Settings
from di import resolve


def test_required_settings() -> None:
    """Test ensure that the required variables are set."""
    settings = resolve(Settings)
    assert settings.DB_NAME is not None
    assert isinstance(settings.DB_NAME, str)
