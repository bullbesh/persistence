# persistence
Telegram бот для предприятия Северсталь
 
Адрес бота в Telegram: @severstalxxl_bot

## Использование бота
### Установка зависимостей
Для запуска бота нужен [Poetry](https://github.com/python-poetry/poetry).

Зависимости проекта устанавливаются командой `poetry install`.

### Переменные окружения
Для запуска нужен токен бота - его нужно записать в `.env` файл главной директории, переменные из этого файла будут читаться при помощи плагина [poetry-dotenv-plugin](https://github.com/mpeteuil/poetry-dotenv-plugin)

### Запуск бота
Если все шаги выше выполнены, то запустить бота можно командой `poetry run bot`
