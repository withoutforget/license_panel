from litestar.plugins.sqlalchemy import repository
from sqlalchemy.ext.asyncio import AsyncSession

from src.infra.database.tables.key import Key


class KeyRepository(repository.SQLAlchemyAsyncRepository[Key]):
    def __init__(self, session: AsyncSession):
        super().__init__(session=session)

    model_type = Key
