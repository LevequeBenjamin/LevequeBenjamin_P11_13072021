"""
conftest.py
"""

# import
import json
from multiprocessing import Process
import pytest
from selenium import webdriver
import geckodriver_autoinstaller
from selenium.webdriver.firefox.options import Options
from gudlftapp import server
from gudlftapp.get_data import get_data


# Check if the current version of geckodriver exists
# and if it doesn't exist, download it automatically,
# then add geckodriver to path
geckodriver_autoinstaller.install()


class BaseFixture:
    """This is class for create fixture."""

    @staticmethod
    @pytest.fixture()
    def client():
        """Create Fixture client."""
        with server.app.test_client() as client:
            yield client

    @staticmethod
    @pytest.fixture(scope="module")
    def clubs(tmp_path_factory):
        """Create Fixture clubs."""
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

    @staticmethod
    @pytest.fixture(scope="module")
    def competitions(tmp_path_factory):
        """Create Fixture competitions."""
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

    @staticmethod
    @pytest.fixture(scope="module")
    def database(clubs, competitions):
        """Create Fixture database."""
        get_data.DB_CLUBS_PATH = clubs[0]
        get_data.DB_COMPETITIONS_PATH = competitions[0]

        get_data.load()
        return get_data


class Driver:
    """This is class for create fixture."""

    @staticmethod
    @pytest.fixture(scope="module")
    def driver(database):
        """Create Fixture driver Firefox."""
        process = Process(target=server.app.run)
        process.daemon = True
        process.start()

        options = Options()
        options.add_argument("--headless")
        options.add_argument("--width=1920")
        options.add_argument("--height=1080")
        driver = webdriver.Firefox(options=options)
        driver.get("http://127.0.0.1:5000")
        return driver
