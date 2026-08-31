# API Tests for DummyJSON

Набор автотестов для публичного API DummyJSON (эндпоинты Auth и Carts), написанный на Python + pytest.

| Coverage | Design | Stack |
|---|---|---|
| Authentication and cart CRUD, including negative authorization and missing-resource scenarios | Reusable fixtures and independent tests that assert status codes and response contracts | Python 3.12, pytest, requests |

## Быстрый старт

```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
pytest -v
```

## Покрытие

- **Auth:** успешный и неуспешный вход, получение профиля с токеном и без него.
- **Carts:** получение, создание, обновление и удаление корзины.
- **Negative paths:** неверные credentials, отсутствующая авторизация и несуществующий ресурс.

## Структура проекта

```
DummyJSON_Test/
├── tests/
│   ├── test_auth.py      # Тесты авторизации
│   └── test_carts.py     # Тесты корзин
├── conftest.py           # Фикстуры pytest (получение токена)
├── requirements.txt      # Зависимости
└── README.md             # Документация
```

## Особенности реализации

- API DummyJSON является фейковым (in-memory database)
- При DELETE корзина помечается как `isDeleted: true`, но не удаляется физически
- При PUT используется параметр `merge: true` для корректного слияния товаров
- Тесты не зависят друг от друга (кроме фикстуры получения токена)

## Примечание по поведению API

В процессе выполнения задания были выявлены особенности поведения DummyJSON, которые учтены в тестах:
- API возвращает поле `accessToken` вместо ожидаемого `token` — тесты адаптированы под реальную схему ответа.
- При неверном пароле API возвращает статус `400 Bad Request` вместо стандартного `401 Unauthorized` — проверка учитывает эту особенность.
