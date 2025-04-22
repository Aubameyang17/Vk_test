import pytest
import requests
from config import BASE_URL, USERNAME, PASSWORD

@pytest.fixture(scope="session")
def auth_token():
    response = requests.post(
        f"{BASE_URL}/users/login",
        json={"login_id": USERNAME, "password": PASSWORD}
    )
    assert response.status_code == 200, "Не удалось авторизоваться"
    return response.headers["Token"]
