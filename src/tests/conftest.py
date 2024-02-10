from typing import Iterator

import pytest
from sqlalchemy import create_engine
from sqlalchemy.engine import Engine

from app.core.settings import settings
from app.core.utils import tmp_database


@pytest.fixture(scope="session")
def pg_url() -> str:
    """
    Provides base PostgreSQL URL for creating temporary databases.
    """
    settings.DB_HOST = "localhost"
    return settings.database_uri  # type: ignore


@pytest.fixture()
def postgres(pg_url: str) -> Iterator[str]:
    """
    Creates empty temporary database.
    """
    with tmp_database(
        pg_url, suffix="main", template=settings.DB_NAME
    ) as tmp_url:
        yield tmp_url


@pytest.fixture()
def postgres_engine(
    postgres: str,
) -> Iterator[Engine]:
    """
    SQLAlchemy engine, bound to temporary database.
    """
    engine = create_engine(postgres, echo=True)
    try:
        yield engine
    finally:
        engine.dispose()
