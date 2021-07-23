"""Docstrings."""

from gudlft.get_data import get_data


class TestGetData:
    def setup_method(self):
        self.club1_by_mail = get_data.get_club_by_mail(mail="test1@test.com")
        self.club2_by_mail = get_data.get_club_by_mail(mail="test2@test.com")
        self.club_none_by_mail = get_data.get_club_by_mail(mail="foo")
        self.club1_by_name = get_data.get_club_by_name(name="Club Test 1")
        self.club2_by_name = get_data.get_club_by_name(name="Club Test 2")
        self.club_none_by_name = get_data.get_club_by_name(name="foo")
        self.competition1 = get_data.get_competition_by_name(name="Competition Test 1")
        self.competition2 = get_data.get_competition_by_name(name="Competition Test 2")
        self.competition_none = get_data.get_competition_by_name(name="foo")

    def test_load_clubs(self, database, clubs):
        """Docstrings."""
        assert database.CLUBS == clubs[1]["clubs"]

    def test_load_competitions(self, database, competitions):
        """Docstrings."""
        assert database.COMPETITIONS == competitions[1]["competitions"]

    def test_get_club_by_mail(self, database):
        """Docstrings."""
        assert self.club1_by_mail == database.CLUBS[0]
        assert self.club2_by_mail == database.CLUBS[1]
        assert self.club_none_by_mail is None

    def test_get_club_by_name(self, database):
        """Docstrings."""
        assert self.club1_by_name == database.CLUBS[0]
        assert self.club2_by_name == database.CLUBS[1]
        assert self.club_none_by_name is None

    def test_get_competition_by_name(self, database):
        """Docstrings."""
        assert self.competition1 == database.COMPETITIONS[0]
        assert self.competition2 == database.COMPETITIONS[1]
        assert self.competition_none is None

    def test_load(self, database, clubs, competitions):
        """Docstrings."""
        assert database.CLUBS == clubs[1]["clubs"]
        assert database.COMPETITIONS == competitions[1]["competitions"]
