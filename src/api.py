

import os
import requests
from dotenv import load_dotenv

# Load API key from the .env file in the project root
load_dotenv()

API_KEY = os.getenv("API_FOOTBALL_KEY")

BASE_URL = "https://v3.football.api-sports.io"

headers = {
    "x-apisports-key": API_KEY
}


def search_teams(team_name):
    """Search for football teams by name."""

    url = f"{BASE_URL}/teams"

    params = {
        "search": team_name
    }

    try:
        response = requests.get(
            url,
            headers=headers,
            params=params,
            timeout=15
        )

        data = response.json()

        if response.status_code == 200:
            if data.get("errors"):
                print("API Error:", data["errors"])
                return []

            return data.get("response", [])

        print("API Error:", response.status_code)
        print(data.get("errors", response.text))
        return []

    except requests.exceptions.RequestException as error:
        print("Connection error:", error)
        return []

    except ValueError:
        print("Error: API returned invalid JSON.")
        return []


def get_matches(team_id):
    """Retrieve the team's 10 most recent finished matches."""

    url = f"{BASE_URL}/fixtures"

    params = {
        "team": team_id,
        "last": 20
    }

    try:
        response = requests.get(
            url,
            headers=headers,
            params=params,
            timeout=15
        )

        data = response.json()

        if response.status_code == 200:
            if data.get("errors"):
                print("API Error:", data["errors"])
                return []

            fixtures = data.get("response", [])

            # Keep only completed matches
            finished_statuses = ["FT", "AET", "PEN"]

            matches = [
                fixture for fixture in fixtures
                if fixture["fixture"]["status"]["short"]
                in finished_statuses
            ]

            # Sort newest first
            matches.sort(
                key=lambda match: match["fixture"]["date"],
                reverse=True
            )

            return matches[:10]

        print("API Error:", response.status_code)
        print(data.get("errors", response.text))
        return []

    except requests.exceptions.RequestException as error:
        print("Connection error:", error)
        return []

    except ValueError:
        print("Error: API returned invalid JSON.")
        return []
