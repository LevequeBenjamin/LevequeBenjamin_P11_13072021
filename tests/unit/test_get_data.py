"""test_get_data.py"""

from gudlft.get_data import get_data
from tests.conftest import BaseFixture


class TestLoadClubs(BaseFixture):
    """This is class for load clubs tests."""

    @staticmethod
    def test_load_clubs(database, clubs):
        """Test as load_clubs function."""
        assert database.CLUBS == clubs[1]["clubs"]

    @staticmethod
    def test_get_club_by_mail(database):
        """Test as get_club_by_mail function."""
        # Tests with a valid email.
        assert get_data.get_club_by_mail(mail=database.CLUBS[0]['email']) == database.CLUBS[0]
        assert get_data.get_club_by_mail(mail=database.CLUBS[1]['email']) == database.CLUBS[1]

    @staticmethod
    def test_get_club_by_mail_is_none():
        """Test as get_club_by_mail function."""
        # Test with a unknown email.
        assert get_data.get_club_by_mail(mail="foo") is None
        # Test with a empty email.
        assert get_data.get_club_by_mail(mail="") is None
        # Test with a int.
        assert get_data.get_club_by_mail(mail=1) is None
        # Test with a bool.
        assert get_data.get_club_by_mail(mail=True) is None
        # Test with a dict.
        assert get_data.get_club_by_mail(mail={}) is None

    @staticmethod
    def test_get_club_by_name(database):
        """Test as get_club_by_name function."""
        # Tests with a valid name.
        assert get_data.get_club_by_name(name=database.CLUBS[0]['name']) == database.CLUBS[0]
        assert get_data.get_club_by_name(name=database.CLUBS[1]['name']) == database.CLUBS[1]

    @staticmethod
    def test_get_club_by_name_is_none():
        """Test as get_club_by_name function."""
        # Test with a unknown name.
        assert get_data.get_club_by_name(name="foo") is None
        # Test with a empty name.
        assert get_data.get_club_by_name(name="") is None
        # Test with a int.
        assert get_data.get_club_by_name(name=1) is None
        # Test with a bool.
        assert get_data.get_club_by_name(name=True) is None
        # Test with a dict.
        assert get_data.get_club_by_name(name={}) is None


class TestLoadCompetitions(BaseFixture):
    """This is class for load competitions tests."""

    @staticmethod
    def test_load_competitions(database, competitions):
        """Test as load_competitions function."""
        assert database.COMPETITIONS == competitions[1]["competitions"]

    @staticmethod
    def test_get_competition_by_name(database):
        """Test as get_competition_by_name function."""
        # Tests with a valid name.
        assert get_data.get_competition_by_name(name=database.COMPETITIONS[0]['name']) == database.COMPETITIONS[0]
        assert get_data.get_competition_by_name(name=database.COMPETITIONS[1]['name']) == database.COMPETITIONS[1]

    @staticmethod
    def test_get_competition_by_name_is_none():
        """Test as get_competition_by_name function."""
        # Test with a unknown name.
        assert get_data.get_competition_by_name(name="foo") is None
        # Test with a empty name.
        assert get_data.get_competition_by_name(name="") is None
        # Test with a int.
        assert get_data.get_competition_by_name(name=1) is None
        # Test with a bool.
        assert get_data.get_competition_by_name(name=True) is None
        # Test with a dict.
        assert get_data.get_competition_by_name(name={}) is None


class TestLoad(BaseFixture):
    """This is class for load tests."""

    @staticmethod
    def test_load(database, clubs, competitions):
        """Test as load function."""
        # CLUBS
        assert database.CLUBS == clubs[1]["clubs"]
        # COMPETITIONS
        assert database.COMPETITIONS == competitions[1]["competitions"]
