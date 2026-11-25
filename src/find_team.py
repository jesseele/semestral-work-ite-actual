
def find_team(team_name, teams):
    """Find a football team by its name."""

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
