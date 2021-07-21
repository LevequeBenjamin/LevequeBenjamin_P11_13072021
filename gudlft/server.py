"""Docstrings."""

from flask import Flask, render_template, request, redirect, flash, url_for
from gudlft.get_data.get_data import CLUBS, get_competition_by_name, get_club_by_name, COMPETITIONS, get_club_by_mail
from gudlft.utils.utils import is_purchase_valid


app = Flask(__name__)
app.secret_key = 'something_special'


@app.route('/')
def index():
    """Docstrings."""
    return render_template('index.html')


@app.route('/showSummary', methods=['POST'])
def show_summary():
    """Docstrings."""
    found_club = get_club_by_mail(mail=request.form["email"])
    if found_club:
        return render_template('welcome.html', club=found_club, competitions=COMPETITIONS)
    flash("Sorry, that email wasn't found.")
    return render_template('index.html')


@app.route('/book/<competition>/<club>')
def book(competition, club):
    """Docstrings."""
    found_competition = get_competition_by_name(name=competition)
    found_club = get_club_by_name(name=club)

    if found_club and found_competition:
        return render_template('booking.html', club=found_club, competition=found_competition)
    flash("Something went wrong-please try again")
    return render_template('welcome.html', club=club, competitions=COMPETITIONS)


@app.route('/purchasePlaces', methods=['POST'])
def purchase_places():
    """Docstrings."""
    found_competition = get_competition_by_name(name=request.form["competition"])
    found_club = get_club_by_name(name=request.form["club"])
    places_required = request.form['places']

    purchase_is_valid = is_purchase_valid(
        competition=found_competition,
        club=found_club,
        places=places_required,)

    if purchase_is_valid:
        found_competition['numberOfPlaces'] = int(found_competition['numberOfPlaces']) - int(places_required)
        found_club['points'] = int(found_club['points']) - int(places_required)
        flash('Great-booking complete!')
    else:
        flash("Something went wrong-please try again")
    return render_template('welcome.html', club=found_club, competitions=COMPETITIONS)


# TODO: Add route for points display


@app.route('/logout')
def logout():
    """Docstrings."""
    return redirect(url_for('index'))
