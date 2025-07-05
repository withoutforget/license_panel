from src.application.utils.export import export
from src.application.schemas.user import UserAuthSchema, UserRegisterSchema, UserSchema
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
@post("/me")
async def me(user: FromDishka[UserSchema]) -> dict:
    return {"id": user.id, "username": user.username}
