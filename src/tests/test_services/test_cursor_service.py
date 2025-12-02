from di import resolve
from services.database import QueryService


def test_query_service() -> None:
    """Test ensure than query service works correctly."""

    resolve(QueryService)(
        sql='''
    INSERT INTO movie VALUES
    ('Аватар', 2015, 9.9)
    '''
    )
