from src.main.web import get_app
from src.config import config
from src.infra.logging import setup_logger

setup_logger(config.logging)

app = get_app(config)

__all__ = [
    "app",
]
