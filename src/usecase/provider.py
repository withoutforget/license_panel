from dishka import Provider, Scope, provide_all

from src.usecase.auth.login import LoginUsecase
from src.usecase.auth.register import RegisterUsecase


class UsecaseProvider(Provider):
    _get_usecases = provide_all(
        LoginUsecase,
        RegisterUsecase,
        scope=Scope.REQUEST,
    )
