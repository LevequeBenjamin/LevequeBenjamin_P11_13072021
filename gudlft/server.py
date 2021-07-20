"""Docstrings."""

import json
from flask import Flask, render_template, request, redirect, flash, url_for


def load_clubs():
    """Docstrings."""
    with open('db/clubs.json') as db_clubs:
        list_of_clubs = json.load(db_clubs)['clubs']
        return list_of_clubs


def load_competitions():
    """Docstrings."""
    with open('db/competitions.json') as comps:
        list_of_competitions = json.load(comps)['competitions']
        return list_of_competitions


app = Flask(__name__)
app.secret_key = 'something_special'

competitions = load_competitions()
clubs = load_clubs()


@app.route('/')
def index():
    """Docstrings."""
    return render_template('index.html')


@app.route('/showSummary', methods=['POST'])
def show_summary():
    """Docstrings."""
    # fix ERROR: Entering a unknown email crashes the app #1
    # club = [club for club in clubs if club['email'] == request.form['email']][0]
    for club in clubs:
        if club['email'] == request.form['email']:
            return render_template('welcome.html', club=club, competitions=competitions)
        flash("Sorry, that email wasn't found.")
        return render_template('index.html')


@app.route('/book/<competition>/<club>')
def book(competition, club):
    """Docstrings."""
    found_club = [c for c in clubs if c['name'] == club][0]
    found_competition = [c for c in competitions if c['name'] == competition][0]
    if found_club and found_competition:
        return render_template('booking.html', club=found_club, competition=found_competition)
    flash("Something went wrong-please try again")
    return render_template('welcome.html', club=club, competitions=competitions)


@app.route('/purchasePlaces', methods=['POST'])
def purchase_places():
    """Docstrings."""
    competition = [c for c in competitions if c['name'] == request.form['competition']][0]
    club = [c for c in clubs if c['name'] == request.form['club']][0]
    places_required = int(request.form['places'])
    competition['numberOfPlaces'] = int(competition['numberOfPlaces']) - places_required
    flash('Great-booking complete!')
    return render_template('welcome.html', club=club, competitions=competitions)


# TODO: Add route for points display


@app.route('/logout')
def logout():
    """Docstrings."""
    return redirect(url_for('index'))
