# Подъем инференс-сервера ollama

> Если хотите изменить модель с qwen:0.5b на лубую другую, отредактируйте entrypoint.sh

Следуйте всем шагам из localllm/README.md, но с небольшими изменениями:

1. Поготовьте yc cli и docker на своём компьютере
2. Подготовьте облачный регистр и сервисный аккаунт
3. Соберите контейнер ollama с помощью `cd ollama`, `docker build --platform linux/amd64 -t ollama-yc .`
4. Запуште контейнер в регистр
5. Создайте ноду (с портом 11434)

## Проверка работы 

Для проверки работоспособности инстанса можете во вкладке "Запросы" отправить GET на `/api/ps`. В результате вы получите в ответ список моделей - в начале пустой, чуть позже модели начнут подгружаться.

Если всё ок, далее можете попробовать отправить запрос к ноде или алиасу исползуя питон-скрипт check.py

## Получение iam token

1. В авторизованном CLI выполните команду: `yc iam create-token`

2. Отправьте ваш oauth-токен командой
```bash
curl -X POST \
-d '{"yandexPassportOauthToken":"OAUTH_TOKEN"}' \                           
https://iam.api.cloud.yandex.net/iam/v1/tokens
```