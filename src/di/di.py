import punq
from PyQt6.QtWidgets import QApplication

from config.settings import Settings
from services.database import ConnectionService, CursorService, QueryService
from services.loguru_service import LoguruConfig


def _inject_settings(container: punq.Container) -> None:
    """Register settings."""
    container.register(
        service=Settings,
        instance=Settings(),
        scope='singleton',
    )


def _inject_pyqt(container: punq.Container) -> None:
    """Register Pyqt6 app."""
    container.register(
        service=QApplication,
        instance=QApplication([]),
        scope='singleton',
    )


def _inject_loguru(container: punq.Container) -> None:
    container.register(LoguruConfig)


def _inject_db(container: punq.Container) -> None:
    """Register DB services."""
    container.register(ConnectionService)
    container.register(CursorService)
    container.register(QueryService)


def create_container() -> punq.Container:
    """Create container."""
    container = punq.Container()
    _inject_settings(container)
    _inject_db(container)
    _inject_pyqt(container)
    _inject_loguru(container)
    return container


def resolve[Thing](thing: type[Thing]) -> Thing:
    """Resolve thing dependencies."""
    return container.resolve(thing)  # type: ignore[no-any-return]


container = create_container()
