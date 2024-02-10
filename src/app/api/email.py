from fastapi import APIRouter, BackgroundTasks, Depends, HTTPException
from sqlalchemy.orm import Session

import app.crud.users as users_crud
from app.core.dependency import get_db
from app.core.email_utils import send_email


router = APIRouter(
    prefix="/email",
    tags=["email"],
)


@router.get("/{user_id}", response_model=dict[str, str])
async def read_user(
    user_id: int,
    background_task: BackgroundTasks,
    db: Session = Depends(get_db),
):
    db_user = users_crud.get_user(db, user_id=user_id)
    if db_user is None:
        raise HTTPException(status_code=404, detail="User not found")
    to = db_user.email
    context = {
        "subject": "Greetings from Jinja Email",
        "greeting": f"Hello {to}!",
        "message": "This is a sample email generated using Jinja2.",
        "sender_name": "GOD",
    }
    background_task.add_task(send_email(to, **context))  # type: ignore
    return {"message": "Notification sent in the background"}
