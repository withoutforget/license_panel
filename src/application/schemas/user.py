from pydantic import BaseModel
from uuid import UUID
from datetime import datetime


class UserSchema(BaseModel):
    id: UUID
    username: str
    password_hash: str
    is_banned: bool
    created_at: datetime


class UserAuthSchema(BaseModel):
    username: str
    password_hash: str


class UserRegisterSchema(BaseModel):
    username: str
    password: str
