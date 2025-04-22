import requests
from config import BASE_URL

def test_successful_login():
    res = requests.post(f"{BASE_URL}/users/login", json={
        "login_id": "alex",
        "password": "my_test_password"
    })
    assert res.status_code == 200
    assert "Token" in res.headers

def test_invalid_credentials():
    res = requests.post(f"{BASE_URL}/users/login", json={
        "login_id": "bob",
        "password": "bob12345678"
    })
    assert res.status_code == 401

def test_server_unreachable():
    try:
        requests.post("http://invalid_url", timeout=3)
    except requests.exceptions.RequestException as e:
        assert isinstance(e, requests.exceptions.RequestException)
