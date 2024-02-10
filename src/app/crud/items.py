from sqlalchemy.orm import Session

import app.schemas.items as items_schemas
from app.models.items import Item


def get_items(db: Session, skip: int = 0, limit: int = 100):
    return db.query(Item).offset(skip).limit(limit).all()


def create_user_item(
    db: Session, item: items_schemas.ItemCreate, user_id: int
):
    db_item = Item(**item.model_dump(), owner_id=user_id)
    db.add(db_item)
    db.commit()
    db.refresh(db_item)
    return db_item
