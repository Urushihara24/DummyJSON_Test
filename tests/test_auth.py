import requests
from conftest import BASE_URL


def test_login_success():
    """1. Успешная авторизация"""
    payload = {"username": "emilys", "password": "emilyspass", "expiresInMins": 30}
    response = requests.post(f"{BASE_URL}/auth/login", json=payload)

    assert response.status_code == 200
    data = response.json()
    assert "accessToken" in data, "В ответе отсутствует accessToken"
    assert "refreshToken" in data, "В ответе отсутствует refreshToken"


def test_login_fail_wrong_password():
    """2. Неуспешная авторизация (неверный пароль)"""
    payload = {"username": "emilys", "password": "incorrect_password", "expiresInMins": 30}
    response = requests.post(f"{BASE_URL}/auth/login", json=payload)

    assert response.status_code == 400  # Было 401, API возвращает 400
    assert "message" in response.json()


def test_get_me_success(auth_token):
    """3. Получение текущего пользователя с токеном"""
    headers = {"Authorization": f"Bearer {auth_token}"}
    response = requests.get(f"{BASE_URL}/auth/me", headers=headers)

    assert response.status_code == 200
    data = response.json()
    assert data["username"] == "emilys"
    assert "id" in data


def test_get_me_fail_no_token():
    """4. Получение текущего пользователя без токена"""
    response = requests.get(f"{BASE_URL}/auth/me")

    assert response.status_code == 401
