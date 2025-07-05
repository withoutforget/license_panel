from litestar.plugins.sqlalchemy import repository
from sqlalchemy.ext.asyncio import AsyncSession

from src.infra.database.tables.product_activation import ProductActivation


class ProductActivationRepository(
    repository.SQLAlchemyAsyncRepository[ProductActivation]
):
    def __init__(self, session: AsyncSession):
        super().__init__(session=session)

    model_type = ProductActivation
