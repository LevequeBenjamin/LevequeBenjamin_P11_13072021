"""Docstrings."""
from gudlft.utils import utils


class TestUtils:
    def test_get_max_places(self, database):
        """Docstrings."""
        places_12 = utils.get_max_places(
            competition=database.COMPETITIONS[0], club=database.CLUBS[0]
        )
        places_5 = utils.get_max_places(
            competition=database.COMPETITIONS[1], club=database.CLUBS[1]
        )
        places_1 = utils.get_max_places(
            competition=database.COMPETITIONS[0], club=database.CLUBS[2]
        )

        assert places_12 == 12
        assert places_5 == 5
        assert places_1 == 1

    def test_is_purchase_valid(self, database):
        """Docstrings."""
        purchase_pass = utils.is_purchase_valid(
            competition=database.COMPETITIONS[0],
            club=database.CLUBS[0],
            places="3",
        )
        purchase_too_much_places = utils.is_purchase_valid(
            competition=database.COMPETITIONS[0],
            club=database.CLUBS[2],
            places="5",
        )

        assert purchase_pass
        assert not purchase_too_much_places

        purchase_var_not_set = utils.is_purchase_valid(
            competition=None, club=database.CLUBS[0], places="3"
        )
        purchase_places_not_numeric = utils.is_purchase_valid(
            competition=database.COMPETITIONS[0],
            club=database.CLUBS[0],
            places="foo",
        )

        assert not purchase_var_not_set
        assert not purchase_places_not_numeric

    def test_is_competition_finished(self):
        """Docstrings."""
        date1 = "2000-01-01 10:10:10"
        date2 = "2100-01-01 10:10:10"

        assert utils.is_competition_finished(date=date1)
        assert not utils.is_competition_finished(date=date2)
