from flask import render_template, request, redirect, url_for, flash
from run import app
from models import Pitcher, Pitch, Catcher, caught
from forms import PitchForm, PitcherForm, CatcherForm
from database import db_session

"""REGISTRATION VIEWS"""

"""
Pitcher Registration
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
            form.region.data,
            )
        db_session.add(pitcher)
        db_session.commit()
        
        # need a KeyError exception here to avoid duplicates

        # Change this to redirect to new profile page
        return redirect(url_for('index'))

    return render_template('reg_pitcher.html', form=form)


"""
Catcher Registration
"""
@app.route('/reg_catcher', methods=["GET", "POST"])
def reg_catcher():
    
    form = CatcherForm(request.form)
    
    if request.method == 'POST' and form.validate():
        catcher = Catcher(
            form.developer_name.data,
            form.developer_url.data,
            form.developer_description.data,
            form.interests.data,
            form.frontend_interest.data,
            form.backend_interest.data,
            form.frontend_experience.data,
            form.backend_experience.data,
            form.prog_languages.data,
            form.email.data,
            form.region.data,
            )
        db_session.add(catcher)
        db_session.commit()
        return redirect(url_for('index'))

    return render_template('reg_catcher.html', form=form)


"""
Pitch Registration
"""
@app.route('/reg_pitch', methods=["GET", "POST"])
def reg_pitch():
    
    form = PitchForm(request.form)

    if request.method == 'POST':

        pitch = Pitch(
            form.proposal_name.data,
            form.proposal_outline.data,
            form.interests.data,
            form.launch_date.data,
            form.pitcher_id.data
            )
        print(pitch.pitcher_id)
        print(pitch.launch_date)
        db_session.add(pitch)
        db_session.commit()
        
        # Change this to redirect to an acknowledgement page
        return redirect(url_for('index'))

    sponsor = db_session.query(Pitcher).all()
    return render_template('reg_pitch.html', form=form, sponsor=sponsor)