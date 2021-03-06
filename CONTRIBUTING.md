# Контрибьютинг в проект

Здесь представлены советы по созданию правильного (для нас) пулл-реквеста.

**Одно общее правило - все коммиты и названия пулл-реквестов должны быть на русском языке и с заглавной буквы!**

[Перед всем](#перед-всем)
* [Установка зависимостей](#установка-зависимостей)

[Каким должен быть пулл-реквест по смыслу изменений](#каким-должен-быть-пулл-реквест-по-смыслу-изменений)
* [Правило "добавил/изменил/удалил"](#правило-добавилизменилудалил)
* [Пулл-реквест должен быть единым](#пулл-реквест-должен-быть-единым)

[Как должен называться пулл-реквест](#как-должен-называться-пулл-реквест)
* [Название ветки](#название-ветки)
* [Название пулл-реквеста](#название-пулл-реквеста)

[После пулл-реквеста](#после-пулл-реквеста)
* [Ревью](#ревью)


## Перед всем

### Установка зависимостей

Установите [poetry](https://github.com/python-poetry/poetry) и зависимости (через `poetry install`).

Необязательно, но можно установить [poetry-dotenv-plugin](https://github.com/mpeteuil/poetry-dotenv-plugin)

Теперь можно установить pre-commit с помощью команды `poetry run pre-commit install` (если возникли проблемы с black, то установите переменную среды `PYTHONUTF8=1` и попробуйте заново).

## Каким должен быть пулл-реквест по смыслу изменений

### Правило "добавил/изменил/удалил"

Пулл-реквест должен быть таким, чтобы его можно было охарактеризовать только одним их этих глаголов. Например, пулл-реквест, в котором появлился этот документ - "добавил", а пулл-реквест, в котором исправлена опечатка в докстринге - "изменил".

### Пулл-реквест должен быть единым

Если вы делаете пулл-реквест с созданием новой секции бота, то не надо исправлять опечатку в другом коде, так ваш пулл-реквест потеряет единость изменений.

## Как должен называться пулл-реквест

### Название ветки

Ветки должна начинаться по правилу "добавил/изменил/удалил":
- добавил - `add_`
- изменил - `change_`/`fix_`/`update_`/...
- удалил - `del_`

Далее суть пулл-реквеста в двух-трёх словах:
- обновили зависимости - `update_deps`
- сделали более детальный вывод цен акций - `increase_stock_price_message_verbosity`
- удалили неиспользуемый класс - `del_unused_<ClassName>_class`
- сделали вывод нового вида финансового отчёта - `add_new_finance_report`

### Название пулл-реквеста

Название пулл-реквеста должно начинаться с одного из глаголов "добавил/изменил/удалил", далее в двух-трёх словах об изменениях.

Там же будет шаблон, который вы должны будете заполнить. Пожалуйста, заполняйте всё тщательно, так ваш пулл-реквест будет легче проверять.

## После пулл-реквеста

### Ревью

Пулл-реквест должен пройти как минимум одно ревью, чтобы влиться в основную ветку. Просите ревью у [Masynchin](https://github.com/Masynchin), либо у [bullbesh](https://github.com/bullbesh) или [BobaUbisoft17](https://github.com/BobaUbisoft17)
