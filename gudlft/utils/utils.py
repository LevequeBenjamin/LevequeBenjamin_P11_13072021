"""Docstrings."""

# imports
from datetime import datetime


def get_max_places(club: dict, competition: dict):
    """Docstrings."""
    return min(int(club["points"]), int(competition["numberOfPlaces"]), 12)


def is_purchase_valid(club, competition, places):
    """Docstrings."""
    if not competition or not club:
        return False
    if not places.isnumeric():
        return False
    if not 0 < int(places) <= get_max_places(club=club, competition=competition):
        return False

    return True


def is_competition_finished(date):
    """Docstrings."""
    date_time = datetime.strptime(date, "%Y-%m-%d %H:%M:%S")

    return datetime.today() > date_time
