from dishka import (
    Provider,
    from_context,
    Scope,
    make_async_container,
    AsyncContainer,
    provide_all,
)
from src.application.services.auth import AuthService

from src.config import Config, config

from src.infra.database.provider import DatabaseProvider
from src.usecase.provider import UsecaseProvider


class DishkaProvider(Provider):
    _get_config = from_context(Config, scope=Scope.APP)

    _get_services = provide_all(
        AuthService,
        scope=Scope.REQUEST,
    )


def get_container() -> AsyncContainer:
    return make_async_container(
        DishkaProvider(),
        UsecaseProvider(),
        DatabaseProvider(),
        context={Config: config},
    )


container: AsyncContainer = get_container()
