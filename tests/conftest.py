"""Docstrings."""

import json
import pytest

from gudlft import server
from gudlft.get_data import get_data


@pytest.fixture()
def client():
    """Docstrings."""
    with server.app.test_client() as client:
        yield client


@pytest.fixture(scope="module")
def clubs(tmp_path_factory):
    """Docstrings."""
    clubs = {
        "clubs": [
            {"name": "Club Test 1", "email": "test1@test.com", "points": "20"},
            {"name": "Club Test 2", "email": "test2@test.com", "points": "10"},
            {"name": "Club Test 3", "email": "test3@test.com", "points": "1"},
        ]
    }

    clubs_file_path = tmp_path_factory.getbasetemp() / "clubs.json"

    with open(clubs_file_path, "w") as file:
        json.dump(clubs, file, indent=4)

    return clubs_file_path, clubs


@pytest.fixture(scope="module")
def competitions(tmp_path_factory):
    """Docstrings."""
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

    competitions_file_path = tmp_path_factory.getbasetemp() / "competitions.json"

    with open(competitions_file_path, "w") as file:
        json.dump(competitions, file, indent=4)

    return competitions_file_path, competitions


@pytest.fixture(scope="module")
def database(clubs, competitions):
    """Docstrings."""
    get_data.DB_CLUBS_PATH = clubs[0]
    get_data.DB_COMPETITIONS_PATH = competitions[0]

    get_data.load()
    return get_data
