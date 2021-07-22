from datetime import datetime


def get_max_places(club: dict):
    return min(int(club["points"]), 12)


def is_purchase_valid(club, places):
    if not places.isnumeric():
        return False
    if not 0 < int(places) <= get_max_places(club=club):
        return False

    return True


def is_competition_finished(date):
    date_time = datetime.strptime(date, "%Y-%m-%d %H:%M:%S")

    return datetime.today() > date_time
