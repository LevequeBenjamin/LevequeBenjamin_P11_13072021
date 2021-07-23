import json
from pathlib import Path

DB_CLUBS_PATH = Path(__file__).resolve().parent.parent / "db/clubs.json"
DB_COMPETITIONS_PATH = Path(__file__).resolve().parent.parent / "db/competitions.json"


def load_clubs():
    """Docstrings."""
    with open(DB_CLUBS_PATH) as file:
        return json.load(file)['clubs']


def load_competitions():
    """Docstrings."""
    with open(DB_COMPETITIONS_PATH) as file:
        return json.load(file)['competitions']


def get_club_by_mail(mail: str):
    """Docstrings."""
    selected_club = None
    for club in CLUBS:
        if club["email"] == mail:
            selected_club = club
            break

    return selected_club


def get_club_by_name(name: str):
    """Docstrings."""
    selected_club = None
    for club in CLUBS:
        if club["name"] == name:
            selected_club = club
            break

    return selected_club


def get_competition_by_name(name: str):
    """Docstrings."""
    selected_competition = None
    for competition in COMPETITIONS:
        if competition["name"] == name:
            selected_competition = competition
            break

    return selected_competition


def load():
    global COMPETITIONS
    global CLUBS

    COMPETITIONS = load_competitions()
    CLUBS = load_clubs()


COMPETITIONS = None
CLUBS = None
