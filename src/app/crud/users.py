from sqlalchemy.orm import Session

import app.schemas.users as user_schemas
from app.core.security import get_hash_password
from app.models.users import User


def get_user(db: Session, user_id: int):
    return db.query(User).filter(User.id == user_id).first()


def get_user_by_email(db: Session, email: str):
    return db.query(User).filter(User.email == email).first()


def get_users(db: Session, skip: int = 0, limit: int = 100):
    return db.query(User).offset(skip).limit(limit).all()


def create_user(db: Session, user: user_schemas.UserCreate):
    db_user = User(
        email=user.email, hashed_password=get_hash_password(user.password)
    )
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user
