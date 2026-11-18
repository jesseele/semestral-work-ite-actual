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
  # Show choices if multiple teams match
    if len(matches) > 1:
        print("\nMultiple teams found:")

        for index, team in enumerate(matches, start=1):
            print(f"{index}. {team['name']} (ID: {team['id']})")

        try:
            choice = int(input("\nSelect a team number: "))
            if 1 <= choice <= len(matches):
                return matches[choice - 1]
        except ValueError:
            pass

        return None

    return matches[0]

def get_matches(team_id):
    """Retrieve the team's latest finished matches."""

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
            return response.json().get("matches", [])

        print("API Error:", response.status_code)
        print(response.text)
        return []

    except requests.exceptions.RequestException as error:
        print("Connection error:", error)
        return []

    
def display_matches(matches):
    """Display match information."""

    if not matches:
        print("\nNo finished matches found.")
        return

    print("\n========== RECENT MATCHES ==========\n")

    for match in matches:

        # Format match date
        match_date = datetime.fromisoformat(
            match["utcDate"].replace("Z", "+00:00")
        )

        date = match_date.strftime("%d.%m.%Y")

        # Get team names
        home_team = match["homeTeam"]["name"]
        away_team = match["awayTeam"]["name"]

        # Get final score
        score = match["score"]["fullTime"]
        home_score = score["home"]
        away_score = score["away"]

        competition = match["competition"]["name"]

        print(f"Date: {date}")
        print(f"Competition: {competition}")
        print(f"{home_team} {home_score} - {away_score} {away_team}")
        print("-" * 45)
