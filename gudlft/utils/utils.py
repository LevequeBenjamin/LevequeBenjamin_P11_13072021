

def get_max_places(club: dict):
    return min(int(club["points"]), 12)


def is_purchase_valid(competition, club, places):
    if not competition or not club:
        return False
    if not places.isnumeric():
        return False
    if not 0 < int(places) <= get_max_places(club=club):
        return False

    return True
