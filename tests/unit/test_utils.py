"""Docstrings."""
from gudlft.utils import utils
from tests.conftest import BaseFixture


class TestGetMaxPlaces(BaseFixture):
    """Docstrings."""

    def test_get_max_places(self, database):
        """Docstrings."""
        places_12 = utils.get_max_places(
            competition=database.COMPETITIONS[0], club=database.CLUBS[0]
        )
        assert places_12 == 12

        places_5 = utils.get_max_places(
            competition=database.COMPETITIONS[1], club=database.CLUBS[1]
        )
        assert places_5 == 5

        places_1 = utils.get_max_places(
            competition=database.COMPETITIONS[0], club=database.CLUBS[2]
        )
        assert places_1 == 1


class TestIsPurchase(BaseFixture):
    """Docstrings."""

    def test_is_purchase(self, database):
        """Docstrings."""
        purchase = utils.is_purchase_valid(
            competition=database.COMPETITIONS[0],
            club=database.CLUBS[0],
            places="3",
        )
        assert purchase

    def test_is_purchase_too_much_places(self, database):
        """Docstrings."""
        purchase = utils.is_purchase_valid(
            competition=database.COMPETITIONS[0],
            club=database.CLUBS[2],
            places="5",
        )
        assert not purchase

    def test_is_purchase_var_not_set(self, database):
        """Docstrings."""
        purchase = utils.is_purchase_valid(
            competition=None, club=database.CLUBS[0], places="3"
        )
        assert not purchase

    def test_is_purchase_places_not_numeric(self, database):
        """Docstrings."""
        purchase = utils.is_purchase_valid(
            competition=database.COMPETITIONS[0],
            club=database.CLUBS[0],
            places="foo",
        )
        assert not purchase


class TestIsCompetitionFinished(BaseFixture):
    """Docstrings."""

    def test_is_competition_finished(self):
        """Docstrings."""
        date1 = "2000-01-01 10:10:10"

        assert utils.is_competition_finished(date=date1)

    def test_is_competition_not_finished(self):
        """Docstrings."""
        date2 = "2100-01-01 10:10:10"

        assert not utils.is_competition_finished(date=date2)
