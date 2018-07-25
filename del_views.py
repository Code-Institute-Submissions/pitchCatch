from flask import request, redirect, url_for, flash
from run import app
from models import Pitcher, Pitch, Catcher
from database import db_session

"""DELETE VIEWS"""

"""
Delete Pitcher
"""
@app.route('/delete_pitcher/<movement_name>', methods=['GET', 'POST'])
def delete_pitcher(movement_name):
        pitcher_delete = db_session.query(Pitcher).filter_by(movement_name=movement_name).one()
        db_session.delete(pitcher_delete)
        db_session.commit()
        flash("Pitcher deleted!")
        return redirect(url_for('index'))

"""
Delete Catcher
"""
@app.route('/delete_catcher/<developer_name>', methods=['GET', 'POST'])
def delete_catcher(developer_name):
        catcher_delete = db_session.query(Catcher).filter_by(developer_name=developer_name).one()
        db_session.delete(catcher_delete)
        db_session.commit()
        flash("Catcher deleted!")
        return redirect(url_for('index'))

"""
Delete Pitch
"""
@app.route('/delete_pitch/<proposal_name>', methods=['GET', 'POST'])
def delete_pitch(proposal_name):
        pitch_delete = db_session.query(Pitch).filter_by(proposal_name=proposal_name).one()
        db_session.delete(pitch_delete)
        db_session.commit()
        flash("Pitch deleted!")
        return redirect(url_for('index'))