from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

import app.crud.items as items_crud
import app.schemas.items as items_schemas
from app.core.dependency import get_db


router = APIRouter(
    prefix="/items",
    tags=["items"],
)


@router.post("/users/{user_id}/items/", response_model=items_schemas.Item)
def create_item_for_user(
    user_id: int, item: items_schemas.ItemCreate, db: Session = Depends(get_db)
):
    return items_crud.create_user_item(db=db, item=item, user_id=user_id)


@router.get("/items/", response_model=list[items_schemas.Item])
def read_items(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    items = items_crud.get_items(db, skip=skip, limit=limit)
    return items
