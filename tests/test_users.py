import requests
from config import BASE_URL
from utils import get_user_id_by_username, get_channel_id_by_name, get_team_id_by_name


def test_add_user_to_channel(auth_token):
    headers = {"Authorization": f"Bearer {auth_token}"}

    channel_id = "gatb3wsk4jnnmnrzey11jcw4ay"
    user_id = get_user_id_by_username(auth_token, "alex")


    res = requests.post(
        f"{BASE_URL}/channels/{channel_id}/members",
        json={"user_id": user_id},
        headers=headers
    )

    assert res.status_code in [201, 200, 409]  # 409 — если уже в канале

def test_remove_user_from_channel(auth_token):
    headers = {"Authorization": f"Bearer {auth_token}"}

    channel_id = "your_channel_id_here"
    user_id = "user_id_to_remove"

    res = requests.delete(
        f"{BASE_URL}/channels/{channel_id}/members/{user_id}",
        headers=headers
    )

    assert res.status_code in [200, 404]  # 404 — если уже удален
