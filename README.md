# Микросервис "Игра орел или решка"

Предназначен для интеграции в систему игр, но так же сам по себе является независимой игрой.

Перед запуском необходимо создать файл `.env` по образцу из `.env.example`. Для локального запуска
на http://localhost:8080 при помощи сервиса `Docker`:

```commandline
git clone https://github.com/Eytes/coin_game_service.git
docker compose up -d
```

## Планы на будущее:

- [ ] создание TLS соединения
- [ ] добавление авторизации по jwt токену
- [ ] автоматического удаление монетки из БД (https://stackoverflow.com/questions/51856567/how-to-delete-the-document-in-mongodb-after-3-mins-based-on-created-time-by-pyth?rq=4)
