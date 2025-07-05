from litestar.plugins.sqlalchemy import repository
from sqlalchemy.ext.asyncio import AsyncSession

from src.infra.database.tables.user import User


class UserRepository(repository.SQLAlchemyAsyncRepository[User]):
    def __init__(self, session: AsyncSession):
        super().__init__(session=session)

    model_type = User
