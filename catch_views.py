from flask import render_template, request, redirect, url_for, flash
from run import app
from models import Pitcher, Pitch, Catcher, caught
from forms import PitchForm, PitcherForm, CatcherForm
from database import db_session

"""
Catch Pitch
"""
@app.route('/catch_pitch/<proposal_name>', methods=['GET', 'POST'])
def catch_pitch(proposal_name):
    pitch = db_session.query(Pitch).filter_by(proposal_name=request.form['pitch']).first()
    catcher = db_session.query(Catcher).filter_by(developer_name=request.form['catcher']).first()
    
    # Need exception to catch duplicates

    if catcher not in pitch.pitch_catch:
        pitch.pitch_catch.append(catcher)
        db_session.commit()
        
        return redirect(url_for('pitch_profile', proposal_name=proposal_name))