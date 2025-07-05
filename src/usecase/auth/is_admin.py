from dataclasses import dataclass
from src.application.schemas.user import UserSchema


@dataclass(slots=True)
class IsAdminUsecase:
    async def __call__(self, user: UserSchema) -> bool:
        return user.is_admin
