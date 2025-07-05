from dishka.integrations.litestar import DishkaRouter

from .product import router as product_router

router = DishkaRouter(path="/admin", tags=["Admin"], route_handlers=[product_router])
