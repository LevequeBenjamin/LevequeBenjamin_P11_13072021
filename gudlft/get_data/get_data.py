"""Docstrings."""
import json
from pathlib import Path

DB_CLUBS_PATH = Path(__file__).resolve().parent.parent / "db/clubs.json"
DB_COMPETITIONS_PATH = Path(__file__).resolve().parent.parent / "db/competitions.json"


def load_clubs():
    """Docstrings."""
    try:
        with open(DB_CLUBS_PATH) as file:
            return json.load(file)['clubs']
    except FileNotFoundError:
        return None


def load_competitions():
    """Docstrings."""
    try:
        with open(DB_COMPETITIONS_PATH) as file:
            return json.load(file)['competitions']
    except FileNotFoundError:
        return None


def get_club_by_mail(mail: str):
    """Docstrings."""
    if CLUBS:
        for club in CLUBS:
            if club["email"] == mail:
                return club
    return None


def get_club_by_name(name: str):
    """Docstrings."""
    if CLUBS:
        for club in CLUBS:
            if club["name"] == name:
                return club
    return None


def get_competition_by_name(name: str):
    """Docstrings."""
    if COMPETITIONS:
        for competition in COMPETITIONS:
            if competition["name"] == name:
                return competition
    return None


def load():
    """Docstrings."""
    global COMPETITIONS
    global CLUBS

    COMPETITIONS = load_competitions()
    CLUBS = load_clubs()


COMPETITIONS = None
CLUBS = None
