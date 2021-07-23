

class TestClient:
    """Docstrings."""
    def test_index(self, client):
        """Docstrings."""
        response = client.get("/")

        assert response.status_code == 200
        assert b'Welcome' in response.data


class TestShowSummary:
    """Docstrings."""
    def setup_method(self):
        self.email_valid = "test1@test.com"
        self.email_invalid = "foo@bar.com"

    def test_login(self, client, database):
        """Docstrings."""
        response = client.post('/showSummary', data=dict(
            email=self.email_valid,
        ), follow_redirects=True)

        assert response.status_code == 200
        assert bytes(self.email_valid, 'utf-8') in response.data

    def test_login_invalid(self, client, database):
        """Docstrings."""
        # I test the request with an unknown email.
        response = client.post('/showSummary', data=dict(
            email=self.email_invalid,
        ), follow_redirects=True)

        assert response.status_code == 200
        assert b"Sorry, that email wasn&#39;t found." in response.data

    def test_competitions(self, client, database):
        """Docstrings."""
        response = client.post('/showSummary', data=dict(
            email=self.email_valid,
        ), follow_redirects=True)

        for competition in database.COMPETITIONS:
            assert competition["name"] in str(response.data)

    def test_competitions_invalid(self, client, database):
        """Docstrings."""
        # I test the request with an unknown email.
        response = client.post('/showSummary', data=dict(
            email=self.email_invalid,
        ), follow_redirects=True)

        for competition in database.COMPETITIONS:
            assert competition["name"] not in str(response.data)


class TestBook:
    """Docstrings."""
    def setup_method(self):
        self.competition_name = 'Competition Test 1'
        self.club_name = "Club Test 1"
        self.places = 'Places available: 21'

    def test_booking(self, client, database):
        """Docstrings."""
        response = client.get(f"/book/{self.competition_name}/{self.club_name}")

        assert response.status_code == 200
        assert bytes(self.competition_name, 'utf-8') in response.data
        assert bytes(self.places, 'utf-8') in response.data

    def test_booking_invalid(self, client):
        """Docstrings."""
        response = client.get("/book/Foo/Bar")

        assert response.status_code == 500


class TestPurchasePlaces:
    """Docstrings."""

    def test_booking(self, client, database):
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

    def test_booking_with_15_places(self, client, database):
        """Docstrings."""
        # I test the request with more than 12 places.
        response = client.post('/purchasePlaces', data=dict(
            competition=database.COMPETITIONS[0]["name"],
            club=database.CLUBS[0]['name'],
            places=15
        ), follow_redirects=True)

        assert b'you cannot reserve more than 12' in response.data

    def test_booking_with_club_enough_space_available(self, client, database):
        """Docstrings."""
        # I test the request with a greater number of places than the club is available.
        response = client.post('/purchasePlaces', data=dict(
            competition=database.COMPETITIONS[1]["name"],
            club=database.CLUBS[1]['name'],
            places=10
        ), follow_redirects=True)

        assert b'you cannot reserve more than 12' in response.data

    def test_booking_with_competition_enough_space_available(self, client, database):
        """Docstrings."""
        # I test the request with a greater number of places than the competition is available.
        response = client.post('/purchasePlaces', data=dict(
            competition=database.COMPETITIONS[0]["name"],
            club=database.CLUBS[2]['name'],
            places=2
        ), follow_redirects=True)

        assert b'you cannot reserve more than 12' in response.data

    def test_booking_with_finished_competition(self, client, database):
        """Docstrings."""
        # I test the request with a competition which is finished.
        response = client.post('/purchasePlaces', data=dict(
            competition=database.COMPETITIONS[2]["name"],
            club=database.CLUBS[0]['name'],
            places=15
        ), follow_redirects=True)
        assert b'Something went wrong-please' in response.data


class TestShowClub:
    """Docstrings."""

    def test_clubs(self, client, database):
        """Docstrings."""
        response = client.get("showSummary/clubs")

        assert response.status_code == 200

        for club in database.CLUBS:
            assert club["name"] in str(response.data)


class TestLogin:
    """Docstrings."""
    def test_logout(self, client):
        """Docstrings."""
        response = client.get("/logout", follow_redirects=True)

        assert response.status_code == 200
        assert b'Welcome to the GUDLFT' in response.data
