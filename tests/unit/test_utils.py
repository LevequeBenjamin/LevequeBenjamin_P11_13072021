"""test_utils.py"""

# import
from gudlft.utils import utils
from tests.conftest import BaseFixture


class TestGetMaxPlaces(BaseFixture):
    """This is class for get_max_places tests."""

    def test_get_max_places(self, database):
        """Test as get_max_places function."""
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

    def test_get_max_places_is_none(self, database):
        """Test as get_max_places function."""
        places_with_empty_competition = utils.get_max_places(competition={}, club=database.CLUBS[0])
        assert not places_with_empty_competition

        places_with_list = utils.get_max_places(competition=[], club=database.CLUBS[0])
        assert not places_with_list

        places_with_int = utils.get_max_places(competition=1, club=database.CLUBS[0])
        assert not places_with_int

        places_with_bool = utils.get_max_places(competition=True, club=database.CLUBS[0])
        assert not places_with_bool

        places_with_str = utils.get_max_places(competition="string", club=database.CLUBS[0])
        assert not places_with_str


class TestIsPurchase(BaseFixture):
    """This is class for is_purchase tests."""

    def test_is_purchase(self, database):
        """Test is_purchase function."""
        purchase = utils.is_purchase_valid(
            competition=database.COMPETITIONS[0],
            club=database.CLUBS[0],
            places="3",
        )
        assert purchase

    def test_is_purchase_too_much_places(self, database):
        """Test is_purchase function."""
        purchase = utils.is_purchase_valid(
            competition=database.COMPETITIONS[0],
            club=database.CLUBS[2],
            places="5",
        )
        assert not purchase

    def test_is_purchase_competition_is_none(self, database):
        """Test is_purchase function."""
        purchase = utils.is_purchase_valid(
            competition=None, club=database.CLUBS[0], places="3"
        )
        assert not purchase

    def test_is_purchase_places_not_numeric(self, database):
        """Test is_purchase function."""
        purchase = utils.is_purchase_valid(
            competition=database.COMPETITIONS[0],
            club=database.CLUBS[0],
            places="foo",
        )
        assert not purchase


class TestIsCompetitionFinished(BaseFixture):
    """This is class for is_competition_finished tests."""

    def test_is_competition_finished(self):
        """Test is_competition_finished function."""
        date1 = "2000-01-01 10:10:10"

        assert utils.is_competition_finished(date=date1)

    def test_is_competition_not_finished(self):
        """Test is_competition_finished function."""
        date2 = "2100-01-01 10:10:10"

        assert not utils.is_competition_finished(date=date2)

    def test_is_competition_finished_is_false(self):
        """Test is_competition_finished function."""
        # Test with a int.
        assert not utils.is_competition_finished(date=1)
        # Test with a invalid date.
        assert not utils.is_competition_finished(date="210001-01 10:110")
        # Test with a bool.
        assert not utils.is_competition_finished(date=True)
        # Test with a dict.
        assert not utils.is_competition_finished(date={})
