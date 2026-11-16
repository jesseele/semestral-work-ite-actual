import os
import requests
from dotenv import load_dotenv
from datetime import datetime

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
        response = requests.get(url, headers=headers, timeout=15)

        if response.status_code == 200:
            return response.json().get("teams", [])

        print("API Error:", response.status_code)
        print(response.text)
        return []

    except requests.exceptions.RequestException as error:
        print("Connection error:", error)
        return []

def find_team(team_name, teams):
    """Find a team by its name."""

    matches = []

    for team in teams:
        if team_name.lower() in team["name"].lower():
            matches.append(team)

    if not matches:
        return None

    # Prefer an exact name match
    for team in matches:
        if team_name.lower() == team["name"].lower():
            return team
 