[doc("Запуск compose с параметрами")]
@compose flags="":
    docker compose up {{flags}}
[doc("Линтер")]
@lint:
    uv run ruff check --fix
    uv run ruff format
[doc("Инициализация миграций. Не нужно для разработки")]
@m_init:
    uv run alchemy  --config=src.infra.database.litestar_config.config init ./src/infra/database/migrations
[doc("Создание миграций")]
@m_make:
    uv run alchemy --config=src.infra.database.litestar_config.config make-migrations
[doc("Дроп миграций"), confirm("Вы уверены? Это удалит все данные из базы данных: ")]
@m_drop:
    uv run alchemy --config=src.infra.database.litestar_config.config drop-all 
[doc("Применение миграций")]
@m_up:
    uv run alchemy --config=src.infra.database.litestar_config.config upgrade head
[doc("Откат миграций")]
@m_down:
    uv run alchemy --config=src.infra.database.litestar_config.config downgrade base