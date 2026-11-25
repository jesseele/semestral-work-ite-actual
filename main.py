
from src.api import search_teams, get_matches, API_KEY
from src.find_team import find_team
from src.display_matches import display_matches


def main():
    """Run the Football Results Finder program."""

    print("==============================")
    print("   FOOTBALL RESULTS FINDER")
    print("==============================")

    # Check API key
    if not API_KEY:
        print("API key missing! Check your .env file.")
        return

    # Ask user for a team
    team_name = input(
        "\nEnter a football team: "
    ).strip()

    if len(team_name) < 3:
        print("Please enter at least 3 characters.")
        return

    # Search for the team directly
    teams = search_teams(team_name)

    if not teams:
        print("\nNo teams found. Try another name.")
        return

    # Select the team
    team = find_team(team_name, teams)

    if team is None:
        print("\nNo team selected.")
        return

    print(f"\nSelected team: {team['name']}")

    # Retrieve recent matches
    matches = get_matches(team["id"])

    # Display results
    display_matches(matches)


if __name__ == "__main__":
    main()

