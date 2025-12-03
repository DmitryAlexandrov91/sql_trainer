import os
from dataclasses import dataclass
from typing import Any

from loguru import logger

from config.settings import Settings


@dataclass
class LoguruConfig:
    _settings: Settings

    def __call__(self) -> Any:
        log_file_path = os.path.join(
            self._settings.BASE_DIR, self._settings.LOG_NAME
        )
        logger.add(
            log_file_path,
            format=self._settings.FORMAT_LOG,
            level="INFO",
            rotation=self._settings.LOG_ROTATION
        )
