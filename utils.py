import requests
from config import BASE_URL


def get_user_id_by_username(token: str, username: str) -> str:
    headers = {"Authorization": f"Bearer {token}"}
    response = requests.get(f"{BASE_URL}/users/username/{username}", headers=headers)

    if response.status_code == 200:
        return response.json()["id"]
    else:
        raise Exception(f"Не удалось найти пользователя '{username}' (статус {response.status_code})")


def get_channel_id_by_name(token: str, team_id: str, channel_name: str) -> str:
    headers = {"Authorization": f"Bearer {token}"}
    response = requests.get(
        f"{BASE_URL}/teams/{team_id}/channels/name/{channel_name}",
        headers=headers
    )

    if response.status_code == 200:
        return response.json()["id"]
    else:
        raise Exception(f"Не удалось найти канал '{channel_name}' (статус {response.status_code})")


def get_team_id_by_name(token: str, team_name: str) -> str:
    headers = {"Authorization": f"Bearer {token}"}
    response = requests.get(f"{BASE_URL}/teams/name/{team_name}", headers=headers)

    if response.status_code == 200:
        return response.json()["id"]
    else:
        raise Exception(f"Не удалось найти команду '{team_name}' (статус {response.status_code})")
