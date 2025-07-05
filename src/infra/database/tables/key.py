from src.infra.database.tables.base import base

from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy import DateTime, String, text, UUID, Interval

import uuid
from datetime import datetime, timedelta


class Key(base):
    __tablename__ = "keys"

    id: Mapped[uuid.UUID] = mapped_column(
        UUID(as_uuid=True), primary_key=True, default=uuid.uuid4
    )
    title: Mapped[str] = mapped_column(String(length=256), nullable=False)
    description: Mapped[str] = mapped_column(String(length=2048), nullable=True)
    created_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True), server_default=text("now()")
    )
    expire_after: Mapped[timedelta] = mapped_column(Interval(), nullable=False)
