# Twitch-бот для голосований

## Команды бота:

- `!startrating` — Начало голосования
- `!endrating` — Конец голосования

Голосования доступны только для стримера

## Запуск

Скопируйте `.env.example` в `.env` и отредактируйте `.env` файл, заполнив в нём все переменные окружения:

```bash
cp rating_bot/.env.example rating_bot/.env
```

Для управления зависимостями используется [poetry](https://python-poetry.org/),
требуется Python 3.9.

Установка зависимостей и запуск бота:

```bash
poetry install
poetry run python -m rating_bot
```

