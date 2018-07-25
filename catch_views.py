from flask import request, redirect, url_for, flash
from run import app
from models import Pitcher, Pitch, Catcher
from database import db_session


"""
Catch a Pitch
"""
@app.route('/catch_pitch/<proposal_name>', methods=['GET', 'POST'])
def catch_pitch(proposal_name):
    pitch = db_session.query(Pitch).filter_by(proposal_name=request.form['pitch']).first()
    catcher = db_session.query(Catcher).filter_by(developer_name=request.form['catcher']).first()
    
    if catcher not in pitch.pitch_catch:
        pitch.pitch_catch.append(catcher)
        db_session.commit()
        flash("Pitch caught!")
    
    # catch duplicate entries 
    else:
        db_session.rollback()
        flash("You've already caught this pitch!")
        
    return redirect(url_for('pitch_profile', proposal_name=proposal_name))

            
        

        