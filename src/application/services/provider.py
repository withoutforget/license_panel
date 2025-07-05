from dishka import Provider, provide, Scope
from litestar import Request
import structlog

from src.application.errors import BaseError
from src.infra.database.repository.user import UserRepository
from src.application.services.auth import AuthService
from src.application.schemas.user import UserSchema

logger = structlog.get_logger()


class ServiceProvider(Provider):
    @provide(scope=Scope.REQUEST)
    async def _get_user_schema(
        self, request: Request, auth_service: AuthService, user_repo: UserRepository
    ) -> UserSchema:
        token = request.headers.get("token")
        if not token:
            logger.error("No token provided in request headers")
            raise BaseError("Token is required for authentication")
        payload = await auth_service.verify_token(token)
        logger.info("user payload", payload=payload)
        user = await user_repo.get(payload["id"])
        return UserSchema.model_validate(user, from_attributes=True)
