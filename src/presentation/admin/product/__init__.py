from dishka.integrations.litestar import DishkaRouter


router = DishkaRouter(path="/product", tags=["Product"], route_handlers=[])
