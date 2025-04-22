import requests
from config import BASE_URL

def test_post_message(auth_token):
    headers = {"Authorization": f"Bearer {auth_token}"}

    # Здесь подставь корректный channel_id
    channel_id = "gatb3wsk4jnnmnrzey11jcw4ay"

    res = requests.post(f"{BASE_URL}/posts", json={
        "channel_id": channel_id,
        "message": "Hello from API test!"
    }, headers=headers)

    assert res.status_code == 201
    post_data = res.json()
    assert post_data["message"] == "Hello from API test!"

def test_get_channel_messages(auth_token):
    headers = {"Authorization": f"Bearer {auth_token}"}
    channel_id = "gatb3wsk4jnnmnrzey11jcw4ay"

    res = requests.get(f"{BASE_URL}/channels/{channel_id}/posts", headers=headers)
    assert res.status_code == 200
    posts = res.json().get("posts", {})
    assert isinstance(posts, dict)
