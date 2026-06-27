import requests
from conftest import BASE_URL


def test_get_user_carts():
    """5. Получение корзин пользователя"""
    response = requests.get(f"{BASE_URL}/carts/user/1")

    assert response.status_code == 200
    data = response.json()
    assert "carts" in data
    assert isinstance(data["carts"], list)


def test_get_cart_by_id():
    """6. Получение корзины по id"""
    response = requests.get(f"{BASE_URL}/carts/1")

    assert response.status_code == 200
    data = response.json()
    assert data["id"] == 1
    assert "products" in data


def test_create_cart():
    """7. Создание корзины"""
    payload = {
        "userId": 1,
        "products": [{"id": 1, "quantity": 1}]
    }
    response = requests.post(f"{BASE_URL}/carts/add", json=payload)

    assert response.status_code == 201
    data = response.json()
    assert data["userId"] == 1
    assert len(data["products"]) > 0


def test_update_cart():
    """8. Обновление корзины (PUT)"""
    # В DummyJSON для корректного обновления через PUT/PATCH нужен параметр merge
    payload = {
        "merge": True,
        "products": [{"id": 2, "quantity": 2}]
    }
    response = requests.put(f"{BASE_URL}/carts/1", json=payload)

    assert response.status_code == 200
    assert response.json()["id"] == 1


def test_delete_cart():
    """9. Удаление корзины"""
    response = requests.delete(f"{BASE_URL}/carts/1")

    assert response.status_code == 200
    data = response.json()
    assert data["isDeleted"] is True
    assert data["deletedOn"] is not None


def test_negative_get_non_existent_cart():
    """10. Негативная проверка: получение несуществующей корзины"""
    response = requests.get(f"{BASE_URL}/carts/999999")

    assert response.status_code == 404