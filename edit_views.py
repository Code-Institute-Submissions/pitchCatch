from flask import render_template, request, redirect, url_for, flash
from run import app
from models import Pitcher, Pitch, Catcher
from forms import PitchForm, PitcherForm, CatcherForm
from database import db_session
from sqlalchemy.exc import IntegrityError

"""EDIT PROFILE VIEWS"""

"""
Edit Pitcher
"""
@app.route('/edit_pitcher/<movement_name>', methods=['GET', 'POST'])
def edit_pitcher(movement_name):
    pitcher_edit = db_session.query(Pitcher).filter_by(movement_name=movement_name).first()
    # Prepopulate form with existing data
    form = PitcherForm(request.form, obj=pitcher_edit)
    
    if request.method == 'POST' and form.validate():
        # update record with request.form data
        form.populate_obj(pitcher_edit)
        db_session.commit()
        # update value for movement_name variable to pass to template
        movement_name=pitcher_edit.movement_name
        flash("Changes saved.")
        return redirect(url_for('pitcher_profile', movement_name=movement_name))

    return render_template('edit_pitcher.html', movement_name=movement_name, form=form)

"""
Edit Catcher
"""
@app.route('/edit_catcher/<developer_name>', methods=['GET', 'POST'])
def edit_catcher(developer_name):
    catcher_edit = db_session.query(Catcher).filter_by(developer_name=developer_name).first()
    # Prepopulate form with existing data
    form = CatcherForm(request.form, obj=catcher_edit)
    
    if request.method == 'POST' and form.validate():
        # update record with request.form data
        form.populate_obj(catcher_edit)
        db_session.commit()
        # update value for developer_name variable to pass to template
        developer_name=catcher_edit.developer_name
        flash("Changes saved.")
        return redirect(url_for('catcher_profile', developer_name=developer_name))

    return render_template('edit_catcher.html', developer_name=developer_name, form=form)

"""
Edit Pitch
"""
@app.route('/edit_pitch/<proposal_name>', methods=['GET', 'POST'])
def edit_pitch(proposal_name):
    pitch_edit = db_session.query(Pitch).filter_by(proposal_name=proposal_name).first()
    # Prepopulate form with existing data
    form = PitchForm(request.form, obj=pitch_edit)

    if request.method == 'POST' and form.validate():
        # update record with request.form data
        form.populate_obj(pitch_edit)
        db_session.commit()
        # update value for movement_name variable to pass to template
        proposal_name=pitch_edit.proposal_name
        flash("Changes saved.")
        return redirect(url_for('pitch_profile', proposal_name=proposal_name))

    return render_template('edit_pitch.html', proposal_name=proposal_name, form=form)