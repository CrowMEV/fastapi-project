from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

import app.crud.users as users_crud
import app.schemas.users as users_schemas
from app.core.dependency import get_db


router = APIRouter(
    prefix="/users",
    tags=["users"],
)


@router.post("/", response_model=users_schemas.User)
def create_user(user: users_schemas.UserCreate, db: Session = Depends(get_db)):
    db_user = users_crud.get_user_by_email(db, email=user.email)
    if db_user:
        raise HTTPException(status_code=400, detail="Email already registered")
    return users_crud.create_user(db=db, user=user)


@router.get("/", response_model=list[users_schemas.User])
def read_users(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    users = users_crud.get_users(db, skip=skip, limit=limit)
    return users


@router.get("/{user_id}", response_model=users_schemas.User)
def read_user(user_id: int, db: Session = Depends(get_db)):
    db_user = users_crud.get_user(db, user_id=user_id)
    if db_user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return db_user
