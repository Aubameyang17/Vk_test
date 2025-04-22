import requests
from config import BASE_URL
from utils import get_user_id_by_username, get_channel_id_by_name, get_team_id_by_name
import logging
logger = logging.getLogger()

def test_create_channel(auth_token):
    logger.info("Шаг 4: создание канала")
    headers = {"Authorization": f"Bearer {auth_token}"}
    team_id = get_team_id_by_name(auth_token, "at--t")
    data = {
        "team_id": team_id,
        "name": "anotherchannel",
        "display_name": "Tanotherchannel",
        "type": "O"  # O = public, P = private
    }
    res = requests.post(f"{BASE_URL}/channels", json=data, headers=headers)
    assert res.status_code in [201, 409]  # 409 если уже существует
