"""get_data.py."""

# import
import json
from pathlib import Path

# path
DB_CLUBS_PATH = Path(__file__).resolve().parent.parent / "db/clubs.json"
DB_COMPETITIONS_PATH = Path(__file__).resolve().parent.parent / "db/competitions.json"


def load_clubs():
    """Load club from database.

    Returns:
        (dict): A dictionary containing all the clubs in the database.
        None : if the file is not found.
    """
    try:
        with open(DB_CLUBS_PATH) as file:
            return json.load(file)['clubs']
    except FileNotFoundError:
        return None


def load_competitions():
    """Load competition from database.

    Returns:
        (dict): A dictionary containing all the competitions in the database.
        None : If the file is not found.
    """
    try:
        with open(DB_COMPETITIONS_PATH) as file:
            return json.load(file)['competitions']
    except FileNotFoundError:
        return None


def get_club_by_mail(mail: str):
    """Get the club based on its email address.

    Args:
        mail (str): Club email address.

    Returns:
        club (dict): Club associated with given mail address.
        None: If the club is not found.
    """
    try:
        if CLUBS:
            for club in CLUBS:
                if club["email"] == mail:
                    return club
        return None
    except (ValueError, TypeError, KeyError):
        return None


def get_club_by_name(name: str):
    """Get the club based on its name.

    Args:
        name (str): Club name.

    Returns:
        club (dict): Club associated with given name.
        None: If the club is not found.
    """
    try:
        if CLUBS:
            for club in CLUBS:
                if club["name"] == name:
                    return club
        return None
    except (ValueError, TypeError, KeyError):
        return None


def get_competition_by_name(name: str):
    """Get the competition based on its name.

    Args:
        name (str): Competition name.

    Returns:
        club (dict): Competition associated with given name.
        None: If the competition is not found.
    """
    try:
        if COMPETITIONS:
            for competition in COMPETITIONS:
                if competition["name"] == name:
                    return competition
        return None
    except (ValueError, TypeError, KeyError):
        return None


def load():
    """Initiate clubs and competitions loading."""
    global COMPETITIONS
    global CLUBS

    COMPETITIONS = load_competitions()
    CLUBS = load_clubs()


COMPETITIONS = None
CLUBS = None
