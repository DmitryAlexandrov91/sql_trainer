import sqlite3

import pytest

from di import resolve
from services.database import QueryService


def test_query_service_with_error() -> None:
    """Test ensure than query service raise error."""

    with pytest.raises(sqlite3.OperationalError):
        resolve(QueryService)(
            sql='''
        INSERT INTO movie VALUES
        ('Аватар', 2015, 9.9)
        '''
        )


def test_success_query() -> None:
    """Test ensure that query service works corrctly."""
    resolve(QueryService)(
            sql='''
        CREATE TABLE test (id INT)
        '''
    )
