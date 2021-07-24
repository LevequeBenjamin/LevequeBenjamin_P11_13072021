"""Docstrings."""

from gudlft.get_data import get_data


class TestLoadClubs:
    """Docstrings."""

    def test_load_clubs(self, database, clubs):
        """Docstrings."""
        assert database.CLUBS == clubs[1]["clubs"]

    def test_get_club_by_mail(self, database):
        """Docstrings."""
        assert get_data.get_club_by_mail(mail=database.CLUBS[0]['email']) == database.CLUBS[0]
        assert get_data.get_club_by_mail(mail=database.CLUBS[1]['email']) == database.CLUBS[1]

    def test_get_club_by_mail_is_none(self):
        """Docstrings."""
        assert get_data.get_club_by_mail(mail="foo") is None

    def test_get_club_by_name(self, database):
        """Docstrings."""
        assert get_data.get_club_by_name(name=database.CLUBS[0]['name']) == database.CLUBS[0]
        assert get_data.get_club_by_name(name=database.CLUBS[1]['name']) == database.CLUBS[1]
        assert get_data.get_club_by_name(name="foo") is None

    def test_get_club_by_name_is_none(self):
        """Docstrings."""
        assert get_data.get_club_by_name(name="foo") is None


class TestLoadCompetitions:
    """Docstrings."""

    def test_load_competitions(self, database, competitions):
        """Docstrings."""
        assert database.COMPETITIONS == competitions[1]["competitions"]

    def test_get_competition_by_name(self, database):
        """Docstrings."""
        assert get_data.get_competition_by_name(name=database.COMPETITIONS[0]['name']) == database.COMPETITIONS[0]
        assert get_data.get_competition_by_name(name=database.COMPETITIONS[1]['name']) == database.COMPETITIONS[1]
        assert get_data.get_competition_by_name(name="foo") is None

    def test_get_competition_by_name_is_none(self):
        """Docstrings."""
        assert get_data.get_competition_by_name(name="foo") is None


class TestLoad:
    """Docstrings."""

    def test_load(self, database, clubs, competitions):
        """Docstrings."""
        assert database.CLUBS == clubs[1]["clubs"]
        assert database.COMPETITIONS == competitions[1]["competitions"]
