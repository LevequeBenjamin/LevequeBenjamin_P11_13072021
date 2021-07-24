"""Docstrings."""

from gudlft.get_data import get_data
from tests.conftest import BaseFixture


class TestLoadClubs(BaseFixture):
    """Docstrings."""

    @staticmethod
    def test_load_clubs(database, clubs):
        """Docstrings."""
        assert database.CLUBS == clubs[1]["clubs"]

    @staticmethod
    def test_get_club_by_mail(database):
        """Docstrings."""
        assert get_data.get_club_by_mail(mail=database.CLUBS[0]['email']) == database.CLUBS[0]
        assert get_data.get_club_by_mail(mail=database.CLUBS[1]['email']) == database.CLUBS[1]

    @staticmethod
    def test_get_club_by_mail_is_none():
        """Docstrings."""
        assert get_data.get_club_by_mail(mail="foo") is None

    @staticmethod
    def test_get_club_by_name(database):
        """Docstrings."""
        assert get_data.get_club_by_name(name=database.CLUBS[0]['name']) == database.CLUBS[0]
        assert get_data.get_club_by_name(name=database.CLUBS[1]['name']) == database.CLUBS[1]
        assert get_data.get_club_by_name(name="foo") is None

    @staticmethod
    def test_get_club_by_name_is_none():
        """Docstrings."""
        assert get_data.get_club_by_name(name="foo") is None


class TestLoadCompetitions(BaseFixture):
    """Docstrings."""

    @staticmethod
    def test_load_competitions(database, competitions):
        """Docstrings."""
        assert database.COMPETITIONS == competitions[1]["competitions"]

    @staticmethod
    def test_get_competition_by_name(database):
        """Docstrings."""
        assert get_data.get_competition_by_name(name=database.COMPETITIONS[0]['name']) == database.COMPETITIONS[0]
        assert get_data.get_competition_by_name(name=database.COMPETITIONS[1]['name']) == database.COMPETITIONS[1]
        assert get_data.get_competition_by_name(name="foo") is None

    @staticmethod
    def test_get_competition_by_name_is_none():
        """Docstrings."""
        assert get_data.get_competition_by_name(name="foo") is None


class TestLoad(BaseFixture):
    """Docstrings."""

    @staticmethod
    def test_load(database, clubs, competitions):
        """Docstrings."""
        assert database.CLUBS == clubs[1]["clubs"]
        assert database.COMPETITIONS == competitions[1]["competitions"]
