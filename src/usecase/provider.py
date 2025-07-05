from dishka import Provider, Scope, provide_all

from src.usecase.auth.is_admin import IsAdminUsecase
from src.usecase.auth.login import LoginUsecase
from src.usecase.auth.register import RegisterUsecase


class UsecaseProvider(Provider):
    _get_usecases = provide_all(
        LoginUsecase,
        RegisterUsecase,
        IsAdminUsecase,
        scope=Scope.REQUEST,
    )
