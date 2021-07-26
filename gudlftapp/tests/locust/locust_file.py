"""Docstrings."""
from random import randint
from locust import HttpUser, task, between
from gudlftapp.tests.locust import locust_get_data


class User(HttpUser):
    """Docstrings."""
    wait_time = between(1, 2.5)

    @task(10)
    def get_index(self):
        """Docstrings."""
        self.client.get("/")

    @task(8)
    def login(self):
        """Docstrings."""
        club_num = randint(0, len(_DATABASE.CLUBS) - 1)
        email_address = _DATABASE.CLUBS[club_num]["email"]
        self.client.post("/showSummary", {"email": email_address})

    @task(6)
    def booking_menu(self):
        """Docstrings."""
        competition_num = randint(0, len(_DATABASE.COMPETITIONS) - 1)
        competition = _DATABASE.COMPETITIONS[competition_num]["name"]
        club_num = randint(0, len(_DATABASE.CLUBS) - 1)
        club = _DATABASE.CLUBS[club_num]["name"]
        self.client.get(f"/book/{competition}/{club}")

    @task(3)
    def purchase_places(self):
        """Docstrings."""
        competition_num = randint(0, len(_DATABASE.COMPETITIONS) - 1)
        competition = _DATABASE.COMPETITIONS[competition_num]["name"]
        club_num = randint(0, len(_DATABASE.CLUBS) - 1)
        club = _DATABASE.CLUBS[club_num]["name"]
        places = randint(1, 12)
        self.client.post(
            "/purchasePlaces",
            {"competition": competition, "club": club, "places": places},
        )

    @task(3)
    def logout(self):
        """Docstrings."""
        self.client.get("/logout")

    @task(1)
    def list_clubs(self):
        """Docstrings."""
        self.client.get("/showSummary/clubs")


_DATABASE = locust_get_data.load_db()
locust_get_data.start_server()
