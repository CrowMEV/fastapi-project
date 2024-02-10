from typing import Iterator

import pytest
from fastapi.testclient import TestClient
from sqlalchemy.engine import Engine
from sqlalchemy.orm import Session

from app.core.dependency import get_db
from app.main import app


@pytest.fixture()
def db(postgres_engine: Engine) -> Iterator[Session]:
    with Session(postgres_engine) as session:
        yield session


@pytest.fixture()
def client(db: Session) -> Iterator[TestClient]:
    app.dependency_overrides[get_db] = lambda: db
    with TestClient(app) as c:
        yield c
