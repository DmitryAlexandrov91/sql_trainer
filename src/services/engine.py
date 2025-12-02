from sqlite3 import Connection, Cursor, connect
from dataclasses import dataclass
from contextlib import contextmanager
from typing import Any, Generator
from config.settings import Settings


@dataclass
class ConnectionService:
    _settings: Settings

    @contextmanager
    def __call__(self) -> Generator[Connection, Any, None]:
        conn = connect(self._settings.db_path)
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

    @contextmanager
    def __call__(self, commit=True) -> Generator[Cursor, Any, None]:
        with self._connection() as conn:
            cur = conn.cursor()
            try:
                yield cur
            except Exception:
                cur.connection.rollback()
            finally:
                if commit:
                    cur.connection.commit()
                cur.close()
