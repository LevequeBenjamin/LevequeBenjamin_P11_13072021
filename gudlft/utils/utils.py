from flask import flash


def get_max_places(club: dict):
    return min(int(club["points"]), 12)


def is_purchase_valid(club, places):
    if not places.isnumeric():
        return False
    if not 0 < int(places) <= get_max_places(club=club):
        return False

    return True
