from flask import render_template, request, redirect, url_for, flash
from run import app
from models import Pitcher, Pitch, Catcher, caught
from forms import PitchForm, PitcherForm, CatcherForm
from database import db_session


"""PROFILE VIEWS"""

"""
Pitcher profile
"""
@app.route('/pitcher_profile/<movement_name>', methods=['GET', 'POST'])
def pitcher_profile(movement_name):
    pitcher_profile = db_session.query(Pitcher).filter_by(movement_name=movement_name)

    return render_template('pitcher_profile.html', pitcher_profile=pitcher_profile)

"""
Catcher Profile
"""
@app.route('/catcher_profile/<developer_name>', methods=['GET', 'POST'])
def catcher_profile(developer_name):
    catcher_profile = db_session.query(Catcher).filter_by(developer_name=developer_name)
    
    return render_template('catcher_profile.html', catcher_profile=catcher_profile)

"""
Pitch Profile
"""
# Pitch Profile
@app.route('/pitch_profile/<proposal_name>', methods=['GET', 'POST'])
def pitch_profile(proposal_name):
    pitches_list = db_session.query(Pitch).filter_by(proposal_name=proposal_name).first()
    catcher_select = db_session.query(Catcher).all()
    
    return render_template('pitch_profile.html', 
                            # caught_list=caught_list,
                            catcher_select=catcher_select,
                            pitches_list=pitches_list)