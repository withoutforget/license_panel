from litestar.plugins.sqlalchemy import repository
from sqlalchemy.ext.asyncio import AsyncSession

from src.infra.database.tables.product import Product


class ProductRepository(repository.SQLAlchemyAsyncRepository[Product]):
    def __init__(self, session: AsyncSession):
        super().__init__(session=session)

    model_type = Product
