from dataclasses import dataclass
from src.infra.database.tables.user import User
from src.infra.database.transaction_manager import SQLAlchemyTransactionManager
from src.application.services.auth import AuthService
from src.application.schemas.user import UserRegisterSchema
from src.infra.database.repository.user import UserRepository

from structlog import get_logger

logger = get_logger()


@dataclass(slots=True)
class RegisterUsecase:
    user_repo: UserRepository
    auth_service: AuthService
    transaction_manager: SQLAlchemyTransactionManager

    async def __call__(self, user_schema: UserRegisterSchema) -> None:
        async with self.transaction_manager:
            pass_hash = await self.auth_service.hash_password(user_schema.password)
            user = await self.user_repo.add(
                User(username=user_schema.username, password_hash=pass_hash)
            )
            logger.info("user registered", user=user)
