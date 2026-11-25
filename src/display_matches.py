
from datetime import datetime


def display_matches(matches):
    """Display the team's recent match results."""

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

        # Get competition name
        competition = match["competition"]["name"]

        print(f"Date: {date}")
        print(f"Competition: {competition}")
        print(f"{home_team} {home_score} - {away_score} {away_team}")
        print("-" * 45)
