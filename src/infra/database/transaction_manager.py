from dataclasses import dataclass
from sqlalchemy.ext.asyncio import AsyncSession


@dataclass(slots=True)
class SQLAlchemyTransactionManager:
    session: AsyncSession

    async def __aenter__(self):
        await self.session.begin()

    async def __aexit__(self, exc_type, exc_val, exc_tb):
        if exc_type is not None:
            await self.session.rollback()
            return False
        await self.session.commit()
        return True
