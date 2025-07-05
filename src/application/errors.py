from litestar import status_codes


class BaseError(Exception):
    def __init__(
        self,
        message="An unknown error occurred.",
        status_code: int = status_codes.HTTP_500_INTERNAL_SERVER_ERROR,
    ) -> None:
        self.status_code = status_code
        self.message = message

    def __str__(self) -> str:
        return self.message
