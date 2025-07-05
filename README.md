<h2 align="center">License Panel🚀</h1>

<div align="center">

[![Python 3.13](https://img.shields.io/badge/Python-3.13-blue.svg)](https://python.org)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Litestar](https://img.shields.io/badge/Framework-Litestar-blueviolet.svg)](https://litestar.dev)

</div>

___

<p align="justify"> REST-API реализующее backend системы лицензирования для проектов.
</p>

### 🛠 Стек технологий
- **Python** 3.13
- **Web Framework**: Litestar
- **ORM**: SQLAlchemy + Advanced Alchemy
- **DI**: Dishka
- **Database**: PostgreSQL
### Зависимости для разработки
- [direnv](https://direnv.net/) + [shell hook](https://direnv.net/docs/hook.html)
- [just](https://github.com/casey/just)

### Установка
После захода в директорию необходимо прописать `direnv allow`
```bash
git clone git@github.com:withoutforget/license_panel.git 
cd license_panel
cp infra/example.config.toml infra/config.toml
uv venv && uv sync
uv run pre-commit install
```
### Justfile
Список доступных команд можно посмотреть через `just --list`
или `just -l`.
```bash
Available recipes:
    compose flags="" # Запуск compose с параметрами
    lint             # Линтер
    m_down           # Откат миграций
    m_drop           # Дроп миграций
    m_init           # Инициализация миграций. Не нужно для разработки
    m_make           # Создание миграций
    m_up             # Применение миграций
```