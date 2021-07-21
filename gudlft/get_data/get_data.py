import json


def load_clubs():
    """Docstrings."""
    with open('db/clubs.json') as file:
        return json.load(file)['clubs']


def load_competitions():
    """Docstrings."""
    with open('db/competitions.json') as file:
        return json.load(file)['competitions']


def get_club_by_mail(mail: str):
    selected_club = None
    for club in CLUBS:
        if club["email"] == mail:
            selected_club = club
            break

    return selected_club


def get_club_by_name(name: str):
    selected_club = None
    for club in CLUBS:
        if club["name"] == name:
            selected_club = club
            break

    return selected_club


def get_competition_by_name(name: str):
    selected_competition = None
    for competition in COMPETITIONS:
        if competition["name"] == name:
            selected_competition = competition
            break

    return selected_competition


COMPETITIONS = load_competitions()
CLUBS = load_clubs()
