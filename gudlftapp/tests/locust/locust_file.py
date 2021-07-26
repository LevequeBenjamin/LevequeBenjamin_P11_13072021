"""locust_file.py"""
from random import randint
from locust import HttpUser, task, between
from gudlftapp.tests.locust import locust_get_data

# master.conf in current directory
# locustfile = gudlftapp/tests/locust/locust_file.py
# headless = true
# host = http://127.0.0.1:5000
# users = 6
# spawn-rate = 6
# run-time = 10s
# only-summary = true


class User(HttpUser):
    """
    Here we define a class for the users that we will be simulating.
    It inherits from HttpUser which gives each user a client attribute,
    which is an instance of HttpSession, that can be used to make HTTP
    requests to the target system that we want to load test.
    When a test starts, locust will create an instance
    of this class for every user that it simulates, and each of these users
    will start running within their own green gevent thread.
    """

    # Our class defines a wait_time that will make the simulated users
    # wait between 1 and 2.5 seconds after each task (see below) is executed.
    wait_time = between(1, 2.5)

    @task(10)
    def index(self):
        """Declared a task with the index method with a higher weight (10)."""
        self.client.get("/")

    @task(8)
    def login(self):
        """Declared a task with the show_summary method with a higher weight (8)."""
        club_num = randint(0, len(_DATABASE.CLUBS) - 1)
        email_address = _DATABASE.CLUBS[club_num]["email"]
        self.client.post("/showSummary", {"email": email_address})

    @task(6)
    def book(self):
        """Declared a task with the book method with a higher weight (6)."""
        competition_num = randint(0, len(_DATABASE.COMPETITIONS) - 1)
        competition = _DATABASE.COMPETITIONS[competition_num]["name"]
        club_num = randint(0, len(_DATABASE.CLUBS) - 1)
        club = _DATABASE.CLUBS[club_num]["name"]
        self.client.get(f"/book/{competition}/{club}")

    @task(3)
    def purchase_places(self):
        """Declared a task with the purchase_places method with a higher weight (3)."""
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
        """Declared a task with the logout method with a higher weight (3)."""
        self.client.get("/logout")

    @task(1)
    def show_clubs(self):
        """Declared a task with the show_clubs method with a higher weight (1)."""
        self.client.get("/showSummary/clubs")


_DATABASE = locust_get_data.load_db()
locust_get_data.start_server()
