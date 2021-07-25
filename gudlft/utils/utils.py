"""Docstrings."""

# imports
from datetime import datetime


def get_max_places(club: dict, competition: dict):
    """Get the maximum number of places that can be reserved.

    Args:
        club (dict): A club.
        competition (dict): A competition.

    Returns:
        (int): Maximum number of places.
    """
    try:
        return min(int(club["points"]), int(competition["numberOfPlaces"]), 12)
    except (KeyError, TypeError, ValueError):
        return None


def is_purchase_valid(club: dict, competition: dict, places: str) -> bool:
    """Verify if a purchase request is valid.

    Args:
        club (dict): A club.
        competition (dict): A competition.
        places (str): Number of places to be booked.

    Returns:
        (bool): True if purchase is valid or False.
    """
    if not get_max_places(club=club, competition=competition):
        return False
    if not competition or not club:
        return False
    if not places.isnumeric():
        return False
    if not 0 < int(places) <= get_max_places(club=club, competition=competition):
        return False

    return True


def is_competition_finished(date: str) -> bool:
    """Verify if the competition is finished.

    Args:
        date (str): A date of competition.

    Returns:
        (bool): True if the competition is finished or False.
    """
    try:
        date_time = datetime.strptime(date, "%Y-%m-%d %H:%M:%S")

        return datetime.today() > date_time
    except (ValueError, TypeError):
        return False
