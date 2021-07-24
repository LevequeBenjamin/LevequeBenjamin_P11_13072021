"""Docstrings."""
from tests.conftest import BaseFixture


class TestClient(BaseFixture):
    """Docstrings."""

    @staticmethod
    def test_index(client):
        """Docstrings."""
        response = client.get("/")

        assert response.status_code == 200
        assert b'Welcome' in response.data


class TestShowSummary(BaseFixture):
    """Docstrings."""

    def setup_method(self):
        """Docstrings."""
        self.email_invalid = "foo@bar.com"

    @staticmethod
    def test_login(client, database):
        """Docstrings."""
        response = client.post('/showSummary', data=dict(
            email=database.CLUBS[0]['email'],
        ), follow_redirects=True)

        assert response.status_code == 200
        assert bytes(database.CLUBS[0]['email'], 'utf-8') in response.data

    def test_login_invalid(self, client, database):
        """Docstrings."""
        # I test the request with an unknown email.
        response = client.post('/showSummary', data=dict(
            email=self.email_invalid,
        ), follow_redirects=True)

        assert response.status_code == 200
        assert b"Sorry, that email wasn&#39;t found." in response.data

    @staticmethod
    def test_competitions(client, database):
        """Docstrings."""
        response = client.post('/showSummary', data=dict(
            email=database.CLUBS[0]['email'],
        ), follow_redirects=True)

        for competition in database.COMPETITIONS:
            assert competition["name"] in str(response.data)

    def test_competitions_invalid_email(self, client, database):
        """Docstrings."""
        # I test the request with an unknown email.
        response = client.post('/showSummary', data=dict(
            email=self.email_invalid,
        ), follow_redirects=True)

        for competition in database.COMPETITIONS:
            assert competition["name"] not in str(response.data)


class TestBook(BaseFixture):
    """Docstrings."""

    def setup_method(self):
        """Docstrings."""
        self.places = 'Places available: 21'

    def test_booking(self, client, database):
        """Docstrings."""
        response = client.get(f"/book/{database.COMPETITIONS[0]['name']}/{database.CLUBS[0]['name']}")

        assert response.status_code == 200
        assert bytes(database.COMPETITIONS[0]['name'], 'utf-8') in response.data
        assert bytes(self.places, 'utf-8') in response.data

    @staticmethod
    def test_booking_invalid(client):
        """Docstrings."""
        response = client.get("/book/Foo/Bar")

        assert response.status_code == 500


class TestPurchasePlaces(BaseFixture):
    """Docstrings."""

    @staticmethod
    def test_booking(client, database):
        """Docstrings."""
        initial_places = int(database.COMPETITIONS[0]["numberOfPlaces"])
        initial_points = int(database.CLUBS[0]["points"])

        response = client.post('/purchasePlaces', data=dict(
            competition=database.COMPETITIONS[0]["name"],
            club=database.CLUBS[0]['name'],
            places=5
        ), follow_redirects=True)

        assert response.status_code == 200
        assert b'Great-booking complete!' in response.data
        assert int(database.COMPETITIONS[0]["numberOfPlaces"]) == initial_places - 5
        assert int(database.CLUBS[0]["points"]) == initial_points - 5

    @staticmethod
    def test_booking_with_15_places(client, database):
        """Docstrings."""
        # I test the request with more than 12 places.
        response = client.post('/purchasePlaces', data=dict(
            competition=database.COMPETITIONS[0]["name"],
            club=database.CLUBS[0]['name'],
            places=15
        ), follow_redirects=True)

        assert b'you cannot reserve more than 12' in response.data

    @staticmethod
    def test_booking_with_club_enough_space_available(client, database):
        """Docstrings."""
        # I test the request with a greater number of places than the club is available.
        response = client.post('/purchasePlaces', data=dict(
            competition=database.COMPETITIONS[1]["name"],
            club=database.CLUBS[1]['name'],
            places=10
        ), follow_redirects=True)

        assert b'you cannot reserve more than 12' in response.data

    @staticmethod
    def test_booking_with_competition_enough_space_available(client, database):
        """Docstrings."""
        # I test the request with a greater number of places than the competition is available.
        response = client.post('/purchasePlaces', data=dict(
            competition=database.COMPETITIONS[0]["name"],
            club=database.CLUBS[2]['name'],
            places=2
        ), follow_redirects=True)

        assert b'you cannot reserve more than 12' in response.data

    @staticmethod
    def test_booking_with_finished_competition(client, database):
        """Docstrings."""
        # I test the request with a competition which is finished.
        response = client.post('/purchasePlaces', data=dict(
            competition=database.COMPETITIONS[2]["name"],
            club=database.CLUBS[0]['name'],
            places=15
        ), follow_redirects=True)
        assert b'Something went wrong-please' in response.data


class TestShowClub(BaseFixture):
    """Docstrings."""

    @staticmethod
    def test_clubs(client, database):
        """Docstrings."""
        response = client.get("showSummary/clubs")

        assert response.status_code == 200

        for club in database.CLUBS:
            assert club["name"] in str(response.data)


class TestLogin(BaseFixture):
    """Docstrings."""

    @staticmethod
    def test_logout(client):
        """Docstrings."""
        response = client.get("/logout", follow_redirects=True)

        assert response.status_code == 200
        assert b'Welcome to the GUDLFT' in response.data
