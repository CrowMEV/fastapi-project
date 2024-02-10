from typing import Iterator

from sqlalchemy.orm import Session

from .db import SessionLocal


def get_db() -> Iterator[Session]:
    with SessionLocal() as db:
        yield db
