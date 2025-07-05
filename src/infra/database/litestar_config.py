from advanced_alchemy.config import AlembicAsyncConfig, SQLAlchemyAsyncConfig

from src.config import config

# Create a test config using SQLite
config = SQLAlchemyAsyncConfig(
    connection_string=config.database.dsn,
    alembic_config=AlembicAsyncConfig(
        script_location="./src/infra/database/migrations",
    ),
)
