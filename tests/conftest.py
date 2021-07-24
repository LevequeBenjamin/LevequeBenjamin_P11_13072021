"""Docstrings."""

# import
import json
import pytest
from multiprocessing import Process
from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from gudlft import server
from gudlft.get_data import get_data


class BaseFixture:
    """Docstrings."""

    @pytest.fixture()
    def client(self):
        """Docstrings."""
        with server.app.test_client() as client:
            yield client

    @pytest.fixture(scope="module")
    def clubs(self, tmp_path_factory):
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
    def competitions(self, tmp_path_factory):
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
    def database(self, clubs, competitions):
        """Docstrings."""
        get_data.DB_CLUBS_PATH = clubs[0]
        get_data.DB_COMPETITIONS_PATH = competitions[0]

        get_data.load()
        return get_data


class Driver:
    """Docstrings."""
    @pytest.fixture(scope="module")
    def driver(self, database):
        """Docstrings."""
        p = Process(target=server.app.run)
        p.daemon = True
        p.start()

        options = Options()
        options.add_argument("--headless")
        options.add_argument("--width=1920")
        options.add_argument("--height=1080")
        driver = webdriver.Firefox(options=options)
        driver.get("http://127.0.0.1:5000")
        return driver
