
from src.api import get_teams, get_matches, API_TOKEN
from src.find_team import find_team
from src.display_matches import display_matches


def main():
    """Run the Football Results Finder program."""

    print("==============================")
    print("   FOOTBALL RESULTS FINDER")
    print("==============================")

    # Check API token
    if not API_TOKEN:
        print("API token missing! Check your .env file.")
        return

    # Ask user for a team
    team_name = input("\nEnter a football team: ").strip()

    if not team_name:
        print("Please enter a team name.")
        return

    # Retrieve teams from API
    teams = get_teams()

    if not teams:
        return

    # Find selected team
    team = find_team(team_name, teams)

    if team is None:
        print("\nTeam not found or no team selected.")
        return

    print(f"\nSelected team: {team['name']}")

    # Retrieve team's recent matches
    matches = get_matches(team["id"])

    # Display results
    display_matches(matches)


if __name__ == "__main__":
    main()
