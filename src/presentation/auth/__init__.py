from dishka.integrations.litestar import DishkaRouter

from .auth import routes as auth_routes

router = DishkaRouter(path="/auth", tags=["Auth"], route_handlers=[*auth_routes])
