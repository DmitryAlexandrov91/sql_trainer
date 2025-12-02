import punq

from config.settings import Settings
from services.engine import ConnectionService, CursorService


def _inject_settings(container: punq.Container) -> None:
    """Register settings."""
    container.register(
        Settings,
        instance=Settings(),
        scope='singleton',
    )


def _inject_db(container: punq.Container) -> None:
    """Register DB services."""
    container.register(ConnectionService)
    container.register(CursorService)


def create_container() -> punq.Container:
    """Create container."""
    container = punq.Container()
    _inject_settings(container)
    _inject_db(container)
    return container


def resolve[Thing](thing: type[Thing]) -> Thing:
    """Resolve thing dependencies."""
    return container.resolve(thing)  # type: ignore[no-any-return]


container = create_container()
