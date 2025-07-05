from src.infra.database.tables.base import base

from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy import Boolean, DateTime, String, text, UUID

import uuid
from datetime import datetime


class User(base):
    __tablename__ = "users"

    id: Mapped[uuid.UUID] = mapped_column(
        UUID(as_uuid=True), primary_key=True, default=uuid.uuid4
    )
    username: Mapped[str] = mapped_column(
        String(length=64), unique=True, nullable=False
    )
    password_hash: Mapped[str] = mapped_column(String(length=512), nullable=False)
    is_banned: Mapped[bool] = mapped_column(Boolean(), default=False)
    is_admin: Mapped[bool] = mapped_column(
        Boolean(), default=False, server_default=text("false")
    )
    created_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True), server_default=text("now()")
    )
