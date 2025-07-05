from litestar import Litestar
from litestar.config.cors import CORSConfig
from litestar.logging import LoggingConfig
from litestar.openapi.config import OpenAPIConfig
from litestar.openapi.plugins import SwaggerRenderPlugin, ScalarRenderPlugin
import structlog
from src.config import Config

from dishka.integrations.litestar import setup_dishka

from src.presentation.setup import setup as setup_presentation
from src.presentation.handling import get_handlers
from src.main.di import container


def get_app(config: Config) -> Litestar:
    logger = structlog.get_logger()

    app = Litestar(
        path="/api/v1",
        cors_config=CORSConfig(
            allow_credentials=config.api.allow_credentials,
            allow_origins=config.api.allow_origins,
            allow_headers=config.api.allow_headers,
            allow_methods=config.api.allow_methods,
        ),
        route_handlers=setup_presentation(),
        logging_config=LoggingConfig(configure_root_logger=False),
        openapi_config=OpenAPIConfig(
            title="License Panel",
            path="/docs",
            version="1.0.0",
            render_plugins=[
                SwaggerRenderPlugin(path="/swagger"),
                ScalarRenderPlugin(path="/scalar"),
            ],
        ),
        exception_handlers=get_handlers(),
    )

    setup_dishka(container, app)

    for plugin in app.openapi_config.render_plugins:
        logger.info(
            f"docs available at http://{config.api.host}:{config.api.port}/api/v1/docs{plugin.paths[0]}"
        )

    return app
