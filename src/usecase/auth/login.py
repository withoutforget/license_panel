from dataclasses import dataclass
from litestar import status_codes

from src.application.errors import BaseError
from src.application.services.auth import AuthService
from src.application.schemas.user import UserAuthSchema
from src.infra.database.repository.user import UserRepository

from src.infra.database.transaction_manager import SQLAlchemyTransactionManager


@dataclass(slots=True)
class LoginUsecase:
    user_repo: UserRepository
    auth_service: AuthService
    transaction_manager: SQLAlchemyTransactionManager

    async def __call__(self, user_schema: UserAuthSchema) -> str:
        async with self.transaction_manager:
            user = await self.user_repo.get(
                item_id=user_schema.username, id_attribute="username"
            )
            verify_password = await self.auth_service.verify_password(
                user_schema.password_hash, user.password_hash
            )
            if not verify_password:
                raise BaseError(
                    "Invalid password", status_code=status_codes.HTTP_401_UNAUTHORIZED
                )
            return await self.auth_service.generate_token(
                user.id,
                user.username,
            )
