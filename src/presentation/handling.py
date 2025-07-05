from collections.abc import Callable

import structlog
from litestar import Request, Response
from litestar.exceptions import HTTPException
from advanced_alchemy.exceptions import (
    AdvancedAlchemyError,
    NotFoundError,
    DuplicateKeyError,
)

from src.application.errors import BaseError

logger = structlog.get_logger()


def base_error(request: Request, exception: BaseError) -> Response:
    return Response(
        content={
            "detail": exception.message,
        },
        status_code=exception.status_code,
    )


def unhandled_internal_error(request: Request, exception: Exception) -> Response:
    logger.exception("uncaught exception", exc_info=exception)
    logger.info("unhandled exception", route=request.url)
    return Response(
        content={"message": "Internal server error"},
        status_code=500,
    )


def http_error(request: Request, exception: HTTPException) -> Response:
    # logger.info("unhandled exception", route=request.url)
    return Response(
        content={
            "detail": exception.detail,
            "headers": exception.headers or {},
            "extra": exception.extra or {},
        },
        status_code=exception.status_code,
    )


def alchemy_error(request: Request, exception: AdvancedAlchemyError) -> Response:
    ##logger.info("unhandled exception", route=request.url)
    return Response(
        content={
            "detail": exception.detail,
            "extra": {"className": exception.__class__.__name__},
        },
        status_code=400,
    )


def gen_alchemy_error(ex_cls, status_code=400):
    def alchemy_error(request: Request, exception: AdvancedAlchemyError) -> Response:
        logger.exception("uncaught exception", exc_info=exception)
        return Response(
            content={
                "detail": exception.detail,
                "extra": {"className": exception.__class__.__name__},
            },
            status_code=status_code,
        )

    return alchemy_error


def get_handlers() -> dict[type[Exception], Callable[[Request, Exception], Response]]:
    return {
        AdvancedAlchemyError: alchemy_error,
        HTTPException: http_error,
        Exception: unhandled_internal_error,
        DuplicateKeyError: gen_alchemy_error(DuplicateKeyError, 409),
        NotFoundError: gen_alchemy_error(NotFoundError, 404),
        BaseError: base_error,
    }
