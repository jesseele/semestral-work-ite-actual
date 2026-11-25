
from datetime import datetime


def display_matches(matches):
    """Display the team's recent finished match results."""

    if not matches:
        print("\nNo finished matches found.")
        return

    print("\n========== RECENT MATCHES ==========\n")

    for match in matches:

        # Get match date
        match_date = datetime.fromisoformat(
            match["fixture"]["date"].replace("Z", "+00:00")
        )

        date = match_date.strftime("%d.%m.%Y")

        # Get team names
        home_team = match["teams"]["home"]["name"]
        away_team = match["teams"]["away"]["name"]

        # Get final score
        home_score = match["goals"]["home"]
        away_score = match["goals"]["away"]

        # Get competition name
        competition = match["league"]["name"]

        print(f"Date: {date}")
        print(f"Competition: {competition}")
        print(f"{home_team} {home_score} - "
              f"{away_score} {away_team}")
        print("-" * 45)

