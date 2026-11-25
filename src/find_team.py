
def find_team(team_name, teams):
    """Select the requested team from API search results."""

    if not teams:
        print("No teams found.")
        return None

    # First, look for an exact name match
    for item in teams:
        team = item["team"]

        if team_name.lower() == team["name"].lower():
            return team

    # If no exact match, show the available teams
    print("\nTeams found:")

    for index, item in enumerate(teams, start=1):
        team = item["team"]
        country = team.get("country", "Unknown")

        print(f"{index}. {team['name']} ({country})")

    # Ask user to choose a team
    try:
        choice = int(input("\nSelect a team number: "))

        if 1 <= choice <= len(teams):
            return teams[choice - 1]["team"]

    except ValueError:
        pass

    print("Invalid selection.")
    return None

