# Django Shop - Novikov

Онлайн-магазин на Django для изучения GitFlow и командной разработки.

## Технологии

- Python 3.11+
- Django 5.0
- PostgreSQL (опционально)
- Poetry для управления зависимостями

## Структура веток

- `main` — стабильная production версия
- `develop` — основная ветка разработки
- `test` — ветка для тестирования
- `feature/*` — ветки для новых функций

## Установка

### 1. Клонировать репозиторий

```bash
git clone https://github.com/your-username/django-shop-фамилия.git
cd django-shop-фамилия
git checkout develop
```
2. Установить зависимости
```bash
poetry install
```
3. Применить миграции
```bash
poetry run python manage.py migrate
```
4. Запустить сервер
```bash
poetry run python manage.py runserver
```
Приложение будет доступно по адресу: http://127.0.0.1:8000/
Команды Poetry
# Добавить новую зависимость
```bash
poetry add <package>
```

# Добавить dev зависимость
```bash
poetry add --group dev <package>
```

# Запустить Django команды
```bash
poetry run python manage.py <command>
```

# Войти в виртуальное окружение
```bash
poetry shell
```
Автор:
Новиков Артем

Лицензия:
MIT License