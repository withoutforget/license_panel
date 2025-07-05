from litestar import Router
from dishka.integrations.litestar import DishkaRouter

from .auth import router as test_router
from .admin import router as admin_router


def setup() -> list[Router | DishkaRouter]:
    return [test_router, admin_router]
