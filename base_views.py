from flask import render_template, request, redirect, url_for, flash
from run import app
from models import Pitcher, Pitch, Catcher, caught
from forms import PitchForm, PitcherForm, CatcherForm
from database import db_session


@app.teardown_appcontext
def shutdown_session(exception=None):
    db_session.remove()

"""
Index/Landing Page
"""
@app.route('/')
def index():
    
    pitcher_count = db_session.query(Pitcher).count()
    catcher_count = db_session.query(Catcher).count()
    pitch_count = db_session.query(Pitch).count()
    return render_template('index.html', pitcher_count=str(pitcher_count),
                                        catcher_count=str(catcher_count),
                                        pitch_count=str(pitch_count))


