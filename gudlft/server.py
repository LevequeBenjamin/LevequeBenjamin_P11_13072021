"""Docstrings."""
from datetime import datetime

from flask import Flask, render_template, request, redirect, flash, url_for

from gudlft.get_data import get_data

from gudlft.utils.utils import is_purchase_valid, is_competition_finished

app = Flask(__name__)
app.secret_key = 'something_special'

get_data.load()


@app.route('/')
def index():
    """Docstrings."""
    return render_template('index.html')


@app.route('/showSummary', methods=['POST'])
def show_summary():
    """Docstrings."""
    found_club = get_data.get_club_by_mail(mail=request.form["email"])
    if found_club:
        return render_template('welcome.html', club=found_club, competitions=get_data.COMPETITIONS, datetime=datetime)
    flash("Sorry, that email wasn't found.")
    return render_template('index.html')


@app.route('/book/<competition>/<club>')
def book(competition, club):
    """Docstrings."""
    found_competition = get_data.get_competition_by_name(name=competition)
    found_club = get_data.get_club_by_name(name=club)

    if found_club and found_competition:
        return render_template('booking.html', club=found_club, competition=found_competition)
    flash("Something went wrong-please try again")
    return render_template('welcome.html', club=club, competitions=get_data.COMPETITIONS)


@app.route('/purchasePlaces', methods=['POST'])
def purchase_places():
    """Docstrings."""
    found_competition = get_data.get_competition_by_name(name=request.form["competition"])
    found_club = get_data.get_club_by_name(name=request.form["club"])
    places_required = request.form['places']

    if found_competition and found_competition and not is_competition_finished(found_competition['date']):

        if is_purchase_valid(
                club=found_club,
                competition=found_competition,
                places=places_required):
            found_competition['numberOfPlaces'] = int(found_competition['numberOfPlaces']) - int(places_required)
            found_club['points'] = int(found_club['points']) - int(places_required)
            flash('Great-booking complete!')
        else:
            flash("you cannot reserve more than 12 places or it is possible that you do not have enough points.")
    else:
        flash("Something went wrong-please try again")

    return render_template('welcome.html', club=found_club, competitions=get_data.COMPETITIONS, datetime=datetime)


@app.route("/showSummary/clubs")
def show_clubs():
    """Docstrings."""
    return render_template("clubs.html", clubs=get_data.CLUBS)


@app.route('/logout')
def logout():
    """Docstrings."""
    return redirect(url_for('index'))
