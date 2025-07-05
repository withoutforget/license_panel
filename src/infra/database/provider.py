from dishka import Provider, provide, Scope, provide_all
from sqlalchemy.ext.asyncio import (
    AsyncSession,
    create_async_engine,
    async_sessionmaker,
    AsyncEngine,
)
from structlog import get_logger

from typing import AsyncIterable


from src.infra.database.repository.key import KeyRepository
from src.infra.database.repository.product import ProductRepository
from src.infra.database.repository.product_activation import ProductActivationRepository
from src.infra.database.repository.user import UserRepository
from src.infra.database.transaction_manager import SQLAlchemyTransactionManager
from src.config import Config

logger = get_logger()


class DatabaseProvider(Provider):
    @provide(scope=Scope.APP)
    async def _get_engine(self, config: Config) -> AsyncIterable[AsyncEngine]:
        engine: AsyncEngine | None = None
        try:
            if engine is None:
                engine = create_async_engine(config.database.dsn)

            yield engine
        except ConnectionRefusedError as e:
            logger.error("Error connecting to database", e)
        finally:
            if engine is not None:
                await engine.dispose()

    @provide(scope=Scope.REQUEST)
    async def _get_session(self, engine: AsyncEngine) -> AsyncIterable[AsyncSession]:
        async with async_sessionmaker(engine, expire_on_commit=False)() as session:
            yield session

    @provide(scope=Scope.REQUEST)
    async def _get_transaction_manager(
        self, session: AsyncSession
    ) -> AsyncIterable[SQLAlchemyTransactionManager]:
        yield SQLAlchemyTransactionManager(session)

    _get_repository = provide_all(
        UserRepository,
        ProductRepository,
        KeyRepository,
        ProductActivationRepository,
        scope=Scope.REQUEST,
    )
