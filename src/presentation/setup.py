from litestar import Router
from dishka.integrations.litestar import DishkaRouter

from .auth import router as test_router


def setup() -> list[Router | DishkaRouter]:
    return [test_router]
