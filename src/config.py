from dataclasses import dataclass, field
import os

from adaptix import Retort
from dynaconf import Dynaconf


@dataclass(slots=True)
class APIConfig:
    host: str
    port: int

    debug: bool = False
    allow_origins: list[str] = field(default_factory=list)
    allow_headers: list[str] = field(default_factory=list)
    allow_methods: list[str] = field(default_factory=lambda: ["*"])
    allow_credentials: bool = True


@dataclass(slots=True)
class DatabaseConfig:
    host: str
    port: int
    username: str
    password: str
    database: str
    driver: str = "postgresql+psycopg"

    @property
    def dsn(self) -> str:
        return f"{self.driver}://{self.username}:{self.password}@{self.host}:{self.port}/{self.database}"


@dataclass(slots=True)
class LoggingConfig:
    level: str = "DEBUG"
    human_readable_logs: bool = True


@dataclass(slots=True)
class Config:
    logging: LoggingConfig
    api: APIConfig
    database: DatabaseConfig


def get_config() -> Config:
    dyna = Dynaconf(
        settings_files=[os.getenv("CONFIG_FILE", "./infra/config.toml")],
        envvar_prefix="LP",
        load_dotenv=True,
        environments=True,
        default_env="default",
        merge_enabled=True,
        env_switcher="LP_ENV",
    )

    return Retort().load(
        dyna,
        Config,
    )


config: Config = get_config()
