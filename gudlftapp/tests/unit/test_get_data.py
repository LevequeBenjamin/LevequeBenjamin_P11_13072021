"""test_get_data.py"""
import pytest

from gudlftapp.get_data import get_data
from gudlftapp.tests.conftest import BaseFixture


# # # # # # # # # # # # # # #
#     load_clubs()          #
#     get_club_by_mail()    #
#     get_club_by_name()    #
# # # # # # # # # # # # # # #

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
        assert not get_data.get_club_by_mail(mail="foo")
        # Test with a empty email.
        assert not get_data.get_club_by_mail(mail="")
        # Test with a None email.
        assert not get_data.get_club_by_mail(mail=None)
        # Test with a int.
        assert not get_data.get_club_by_mail(mail=1)
        # Test with a bool.
        assert not get_data.get_club_by_mail(mail=True)
        # Test with a dict.
        assert not get_data.get_club_by_mail(mail={})

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
        assert not get_data.get_club_by_name(name="foo")
        # Test with a empty name.
        assert not get_data.get_club_by_name(name="")
        # Test with a None name.
        assert not get_data.get_club_by_name(name=None)
        # Test with a int.
        assert not get_data.get_club_by_name(name=1)
        # Test with a bool.
        assert not get_data.get_club_by_name(name=True)
        # Test with a dict.
        assert not get_data.get_club_by_name(name={})


# # # # # # # # # # # # # # #
#  load_competitions()      #
#  get_competition_by_mail()#
#  get_club_by_name()       #
# # # # # # # # # # # # # # #

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
        assert not get_data.get_competition_by_name(name="foo")
        # Test with a empty name.
        assert not get_data.get_competition_by_name(name="")
        # Test with a None name.
        assert not get_data.get_competition_by_name(name=None)
        # Test with a int.
        assert not get_data.get_competition_by_name(name=1)
        # Test with a bool.
        assert not get_data.get_competition_by_name(name=True)
        # Test with a dict.
        assert not get_data.get_competition_by_name(name={})


# # # # # # # # # # # # # # #
#           load()          #
# # # # # # # # # # # # # # #

class TestLoad(BaseFixture):
    """This is class for load tests."""

    @staticmethod
    def test_load(database, clubs, competitions):
        """Test as load function."""
        # CLUBS
        assert database.CLUBS == clubs[1]["clubs"]
        # COMPETITIONS
        assert database.COMPETITIONS == competitions[1]["competitions"]
