import json
from multiprocessing import Process
from gudlft.get_data import get_data
from gudlft import server
import tempfile

_COMPETITIONS_FP = tempfile.NamedTemporaryFile()
_CLUBS_FP = tempfile.NamedTemporaryFile()


def create_clubs():
    """Create temporary Clubs file."""
    clubs = {
        "clubs": [
            {"name": "Club Test 1", "email": "test1@test.com", "points": "20"},
            {"name": "Club Test 2", "email": "test2@test.com", "points": "10"},
            {"name": "Club Test 3", "email": "test3@test.com", "points": "1"},
        ]
    }

    clubs_file_path = _CLUBS_FP

    with open(clubs_file_path.name, "w") as file:
        json.dump(clubs, file, indent=4)

    return clubs_file_path.name


def create_competitions():
    """Create temporary Competitions file."""
    competitions = {
        "competitions": [
            {
                "name": "Competition Test 1",
                "date": "2100-03-27 10:00:00",
                "numberOfPlaces": 21,
            },
            {
                "name": "Competition Test 2",
                "date": "2100-03-27 10:00:00",
                "numberOfPlaces": 5,
            },
            {
                "name": "Competition Test 3",
                "date": "2000-03-27 10:00:00",
                "numberOfPlaces": 21,
            },
        ]
    }

    competitions_file_path = _COMPETITIONS_FP

    with open(competitions_file_path.name, "w") as file:
        json.dump(competitions, file, indent=4)

    return competitions_file_path.name


def load_db():
    """Load DB with temporary files."""
    get_data.DB_CLUBS_PATH = create_clubs()
    get_data.DB_COMPETITIONS_PATH = create_competitions()

    get_data.load()

    return get_data


def server_wrapper():
    """Mute Flask stdout and run server."""
    import logging
    import click

    log = logging.getLogger("werkzeug")
    log.setLevel(logging.ERROR)

    def secho(text, file=None, nl=None, err=None, color=None, **styles):
        pass

    def echo(text, file=None, nl=None, err=None, color=None, **styles):
        pass

    click.echo = echo
    click.secho = secho
    server.app.run()


def start_server():
    """Start Flask server process."""
    p = Process(target=server_wrapper)
    p.daemon = True
    p.start()
