from flask import render_template, request, redirect, url_for, flash
from run import app
from models import Pitcher, Pitch, Catcher, caught
from forms import PitchForm, PitcherForm, CatcherForm
from database import db_session


# Queries dict
query_dict = {}

# Query create dict items
def query(k,v):
    query_dict[k]=v


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


"""
Pitcher Registration Page
"""
@app.route('/reg_pitcher', methods=['GET', 'POST'])
def reg_pitcher():
    
    form = PitcherForm(request.form)
    
    if request.method == 'POST' and form.validate():
        pitcher = Pitcher(
            form.movement_name.data,
            form.movement_url.data,
            form.movement_description.data,
            form.interests.data,
            form.email.data,
            form.region.data)
        db_session.add(pitcher)
        db_session.commit()

        # Change this to redirect to new profile page
        return redirect(url_for('index'))

    return render_template('reg_pitcher.html', form=form)