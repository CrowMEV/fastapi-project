from pydantic import BaseModel, ConfigDict, EmailStr

import app.schemas.items as items_schemsas


class UserBase(BaseModel):
    email: EmailStr


class UserCreate(UserBase):
    password: str


class User(UserBase):
    id: int
    is_active: bool
    items: list[items_schemsas.Item] = []

    model_config = ConfigDict(from_attributes=True)
