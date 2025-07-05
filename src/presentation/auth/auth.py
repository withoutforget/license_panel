from src.application.services.auth import AuthService
from src.application.utils.export import export
from src.application.schemas.user import UserAuthSchema, UserRegisterSchema
from src.usecase.auth.login import LoginUsecase
from dishka import FromDishka

from litestar import post

from src.usecase.auth.register import RegisterUsecase

routes = []


@export(routes)
@post("/login")
async def login(data: UserAuthSchema, usecase: FromDishka[LoginUsecase]) -> str:
    return await usecase(data)


@export(routes)
@post("/register")
async def register(
    data: UserRegisterSchema, usecase: FromDishka[RegisterUsecase]
) -> None:
    await usecase(data)


@export(routes)
@post("/me/{token:str}")
async def me(token: str, service: FromDishka[AuthService]) -> dict:
    return await service.verify_token(token)
