from src.infra.database.tables.base import base

from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy import String, UUID

import uuid


class Product(base):
    __tablename__ = "products"

    id: Mapped[uuid.UUID] = mapped_column(
        UUID(as_uuid=True), primary_key=True, default=uuid.uuid4
    )
    title: Mapped[str] = mapped_column(String(length=256), nullable=False)
    description: Mapped[str] = mapped_column(String(length=2048), nullable=True)
