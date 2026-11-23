
import os
import requests
from dotenv import load_dotenv

# Load API token from .env
load_dotenv()

API_TOKEN = os.getenv("FOOTBALL_API_TOKEN")

BASE_URL = "https://api.football-data.org/v4"

headers = {
    "X-Auth-Token": API_TOKEN
}


def get_teams():
    """Retrieve available football teams from the API."""

    url = f"{BASE_URL}/teams"

    try:
        response = requests.get(
            url,
            headers=headers,
            timeout=15
        )

        if response.status_code == 200:
            return response.json().get("teams", [])

        print("API Error:", response.status_code)
        print(response.text)
        return []

    except requests.exceptions.RequestException as error:
        print("Connection error:", error)
        return []


def get_matches(team_id):
    """Retrieve the team's 10 most recent finished matches."""

    url = f"{BASE_URL}/teams/{team_id}/matches"

    params = {
        "status": "FINISHED",
        "limit": 10
    }

    try:
        response = requests.get(
            url,
            headers=headers,
            params=params,
            timeout=15
        )

        if response.status_code == 200:

            matches = response.json().get("matches", [])

            # Sort matches by date, newest first
            matches.sort(
                key=lambda match: match["utcDate"],
                reverse=True
            )

            return matches[:10]

        print("API Error:", response.status_code)
        print(response.text)
        return []

    except requests.exceptions.RequestException as error:
        print("Connection error:", error)
        return []
