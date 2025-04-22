import requests
from config import BASE_URL

def test_create_channel(auth_token):
    headers = {"Authorization": f"Bearer {auth_token}"}
    data = {
        "team_id": "at & t",
        "name": "testchannel",
        "display_name": "Test Channel",
        "type": "O"  # O = public, P = private
    }
    res = requests.post(f"{BASE_URL}/channels", json=data, headers=headers)
    assert res.status_code in [201, 409]  # 409 если уже существует
