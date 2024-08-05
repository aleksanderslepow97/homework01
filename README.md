# Проект 01

## Описание:

Проект 01 - это тестовое веб-приложение на Python для виджета банковских операций.

## Установка:

1. Клонируйте репозиторий:
```
git clone git@github.com:aleksanderslepow97/homework01.git
```
2. Установите зависимости:
```
pip install -r requirements.txt
```
## Использование:

1. Откройте приложение в вашем веб-браузере.
2. Создайте новый проект и начните добавлять задачи.
3. Назначайте сроки выполнения и приоритеты для задач, чтобы эффективно управлять проектами.

## Комманда разработки:

Слепов Александр Сергеевич - backend developer.

## Связь с коммандой разработчиков:

sanya.slepow2015@yandex.ru

## Лицензия:

Этот проект лицензирован и конфиденциален. Для получения дополнительной информации обратитесь к комманде разработчиков.

## Тестирование:

1. Запуск тестирования:
```
pytest
```
2. Запуск тестирования с покрытием:
- При активированном виртуальном окружении:
```
pytest --cov
```
- Через Poetry:
```
poetry run pytest --cov
```
11.1. Проект содержит:
- функцию которая принимает список словарей с банковскими операциями и возвращает ID операции, в которых указана заданная валюта, описание каждой операции.
- функцию - генератор номеров банковских карт.

### Декоратор:
В модуле decorators.py реализована функция логгирования в файл или в консоль

### Библиотеки:
- Модуль содержит функцию, которая принимает на вход путь до JSON-файла и возвращает список словарей с данными о финансовых транзакциях.
- функцию, которая принимает на вход транзакцию и возвращает сумму транзакции (amount) в рублях.

### Добавлено ЛОГИРОВАНИЕ в модулях masks, utils.
- Реализовано ТЕСТИРОВАНИЕ некоторых функций проекта через модуль tests.

### Добавлена функция, которая cчитывает данные о финансовых операциях:
- Реализована функция, которая cчитывает данные о финансовых операциях из CSV файла и преобразует их в список словарей.
- Реализована функция, которая cчитывает данные о финансовых операциях из excel файла и преобразует их в список словарей.

### Добавлены функции:
- функциb, которые отвечают за основную логику проекта и связывает функциональности между собой.
- функцию, которая принимает список словарей с данными о банковских операциях и список категорий операций, и возвращать словарь, в котором ключи — это названия категорий, а значения — это количество операций в каждой категории.
- функцию, которая ринимает на вход список словарей с операциями и список строк с категориями, возвращает словарь, где ключи - категории, а значения - количество операций в этой категории.