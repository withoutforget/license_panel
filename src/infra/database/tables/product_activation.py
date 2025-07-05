from src.infra.database.tables.base import base

from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy import DateTime, ForeignKey, UUID

import uuid
from datetime import datetime


class ProductActivation(base):
    __tablename__ = "product_activations"

    user_id: Mapped[uuid.UUID] = mapped_column(
        UUID(as_uuid=True), ForeignKey("users.id"), primary_key=True
    )
    product_id: Mapped[uuid.UUID] = mapped_column(
        UUID(as_uuid=True), ForeignKey("products.id"), primary_key=True
    )
    expire_at: Mapped[datetime] = mapped_column(DateTime(timezone=True), nullable=False)
