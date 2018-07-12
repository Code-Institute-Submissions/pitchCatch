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
    form.pitcher_id.choices = [(g.id, g.movement_name) for g in Pitcher.query.order_by('movement_name')]

    
    if request.method == 'POST':
        the_pitcher = db_session.query(Pitcher).filter_by(movement_name=request.form['pitcher_id']).one()

        pitch = Pitch(
            form.proposal_name.data,
            form.proposal_outline.data,
            form.interests.data,
            form.launch_date.data,
            pitcher_id=the_pitcher.id
            )
        db_session.add(pitch)
        db_session.commit()

    #     # Change this to redirect to an acknowledgement page
        return redirect(url_for('index'))

    sponsor = db_session.query(Pitcher).all()
    return render_template('reg_pitch.html', form=form, sponsor=sponsor)


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