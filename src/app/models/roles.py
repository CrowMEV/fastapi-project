import enum

from sqlalchemy import true
from sqlalchemy.orm import Mapped, mapped_column

from app.models import Base


class RoleNameChoice(enum.Enum):
    USER = "user"
    ADMIN = "admin"


class Role(Base):
    __tablename__ = "roles"

    name: Mapped[RoleNameChoice] = mapped_column(primary_key=True)
    is_active: Mapped[bool] = mapped_column(
        default=True, server_default=true()
    )
    pretty_name: Mapped[str] = mapped_column(default="", server_default="")
