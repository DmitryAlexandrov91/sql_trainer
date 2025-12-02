from di import resolve
from services.engine import CursorService


def test_cursor_service() -> None:
    """Test ensure than cursor service works correctly."""

    cur = resolve(CursorService)()

    with cur as cur:
        cur.execute(
            '''
INSERT INTO movie VALUES
    ('Аватар', 2015, 9.9)
            ''',
        )
