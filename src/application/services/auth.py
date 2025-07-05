from dataclasses import dataclass
import bcrypt
from uuid import UUID
import jwt

from datetime import datetime, timedelta

from src.application.errors import BaseError
from structlog import get_logger

logger = get_logger()


@dataclass(slots=True)
class AuthService:
    __SECRET_KEY = "secret"

    async def hash_password(self, password: str) -> str:
        return bcrypt.hashpw(password.encode("utf-8"), bcrypt.gensalt()).decode("utf-8")

    async def verify_password(self, password: str, hash: str) -> bool:
        return bcrypt.checkpw(password.encode("utf-8"), hash.encode("utf-8"))

    async def generate_token(self, user_id: UUID, username: str) -> str:
        payload = {
            "id": user_id.hex,
            "username": username,
            "exp": datetime.utcnow() + timedelta(minutes=5),
        }

        token = jwt.encode(
            payload=payload,
            key=self.__SECRET_KEY,
            algorithm="HS256",
        )

        return token

    async def verify_token(self, token: str) -> dict:
        try:
            payload = jwt.decode(
                token,
                self.__SECRET_KEY,
                algorithms=["HS256"],
            )
            return payload
        except (
            jwt.ExpiredSignatureError,
            jwt.InvalidTokenError,
        ) as e:
            logger.exception("token expired or invalid", exc_info=e)
            raise BaseError("Token expired or invalid")
