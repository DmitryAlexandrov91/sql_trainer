from contextlib import contextmanager
from dataclasses import dataclass
from sqlite3 import Connection, Cursor, connect
from typing import Any, Generator

from loguru import logger

from config.settings import Settings
from services.loguru_service import LoguruConfig


@dataclass
class ConnectionService:
    _settings: Settings

    @contextmanager
    def __call__(self) -> Generator[Connection, Any, None]:
        conn = connect(self._settings.DB_PATH)
        try:
            yield conn
        finally:
            conn.close()


@dataclass
class CursorService:
    """Service for generate sqlite3 cursors obj.

    get one optional parameter: commit
    default commit=True
    """
    _connection: ConnectionService
    _logger: LoguruConfig

    @contextmanager
    def __call__(self, commit=True) -> Generator[Cursor, Any, None]:
        with self._connection() as conn:
            cur = conn.cursor()
            try:
                yield cur
            except Exception as e:
                logger.error(e)
                cur.connection.rollback()
                raise e
            finally:
                if commit:
                    cur.connection.commit()
                cur.close()


@dataclass
class QueryService:
    """Service for safety send SQL queryes."""
    _cursor: CursorService

    def __call__(self, sql: str, commit=True) -> Any:
        cur = self._cursor(commit=commit)
        with cur as cur:
            cur.execute(sql)
