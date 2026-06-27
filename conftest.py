import pytest
import requests

BASE_URL = "https://dummyjson.com"

@pytest.fixture(scope="session")
def auth_token():
    """Фикстура для получения токена авторизации (используется emilys / emilyspass)"""
    payload = {
        "username": "emilys",
        "password": "emilyspass",
        "expiresInMins": 30
    }
    response = requests.post(f"{BASE_URL}/auth/login", json=payload)
    assert response.status_code == 200, f"Не удалось получить токен: {response.text}"
    return response.json()["accessToken"]  # Было "token", стало "accessToken"
