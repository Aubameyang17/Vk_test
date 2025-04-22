import requests
from config import BASE_URL
import logging
logger = logging.getLogger()

def test_successful_login():
    logger.info("Шаг 1: Авторизация пользователя")
    res = requests.post(f"{BASE_URL}/users/login", json={
        "login_id": "Ar1517",
        "password": "SQLSETTINGS_DATASOURCE"
    })
    assert res.status_code == 200
    assert "Token" in res.headers

def test_invalid_credentials():
    logger.info("Шаг 2: Авторизация  ложного пользователя")
    res = requests.post(f"{BASE_URL}/users/login", json={
        "login_id": "bob",
        "password": "bob12345678"
    })
    assert res.status_code == 401

def test_server_unreachable():
    logger.info("Шаг 3: проверка доступности другого сервера")
    try:
        requests.post("http://invalid_url", timeout=3)
    except requests.exceptions.RequestException as e:
        assert isinstance(e, requests.exceptions.RequestException)
