from flask import render_template, request, redirect, url_for, flash
from run import app
from models import Pitcher, Pitch, Catcher, caught
from forms import PitchForm, PitcherForm, CatcherForm
from database import db_session




"""Search Dictiontary"""
query_dict = {}


"""Create Search Dictionary Items"""
def query(k,v):
    query_dict[k]=v
    print(query_dict)


"""
Search Pitchers Function
"""
@app.route('/pitchers', methods=['GET', 'POST'])
def search_pitchers():
    
    form = PitcherForm(request.form)
    
    if request.method == 'POST':
        
        query('interests', request.form['interests'])
        query('region', request.form['region'])
        query('movement_name', request.form['movement_name'])
        
        # Remove default values from query filter
        kwargs = {k:v for k,v in query_dict.items() if v != '---'}
        
        pitchers_all = db_session.query(Pitcher).all()
        pitcher_count = db_session.query(Pitcher).filter_by(**kwargs).count()
        pitchers_search = db_session.query(Pitcher).filter_by(**kwargs).order_by(Pitcher.movement_name)
        
        # template for search results
        return render_template('pitchers_search.html', 
                                form=form, 
                                pitchers_all=pitchers_all,
                                pitchers_search=pitchers_search, 
                                pitcher_count=pitcher_count)

    # template for pitchers
    pitcher_count = db_session.query(Pitcher).count()
    pitchers_list = db_session.query(Pitcher).filter_by(movement_name=Pitcher.movement_name).order_by(Pitcher.movement_name)
    return render_template('pitchers.html', 
                            form=form,
                            pitchers_list=pitchers_list,  
                            pitcher_count=str(pitcher_count))

"""
Catchers Search Function
"""
# Query Catchers
@app.route('/catchers', methods=['GET', 'POST'])
def search_catchers():
    
    form = CatcherForm(request.form)
    
    if request.method == 'POST':

        query('region', request.form['region'])
        query('interests', request.form['interests'])
        query('frontend_experience', request.form['frontend_experience'])
        query('backend_experience', request.form['backend_experience'])
        query('developer_name', request.form['developer_name'])
        
        kwargs = {k:v for k,v in query_dict.items() if v != '---'}

        catchers_all = db_session.query(Catcher).all()
        catcher_count = db_session.query(Catcher).filter_by(**kwargs).count()
        catchers_search = db_session.query(Catcher).filter_by(**kwargs).order_by(Catcher.developer_name)      
        
        return render_template('catchers_search.html', 
                        form=form, 
                        catchers_all=catchers_all,
                        catchers_search=catchers_search, 
                        catcher_count=catcher_count)
    
    catcher_count = db_session.query(Catcher).count()
    catchers_list = db_session.query(Catcher).filter_by(developer_name=Catcher.developer_name).order_by(Catcher.developer_name)
    return render_template('catchers.html', 
                            catchers_list=catchers_list, 
                            catcher_count=catcher_count, 
                            form=form)


"""
Pitches Search Function
"""
@app.route('/pitches', methods=['GET', 'POST'])
def search_pitches():
    
    form = PitchForm(request.form)
    
    if request.method == 'POST':
        
        # change
        query('interests', request.form['interests'])
        query('proposal_name', request.form['proposal_name'])
        
        # Remove default values from query filter
        kwargs = {k:v for k,v in query_dict.items() if v != '---'}
    
        pitches_all = db_session.query(Pitch).all()
        pitch_count = db_session.query(Pitch).filter_by(**kwargs).count()
        pitches_search = db_session.query(Pitch).filter_by(**kwargs).order_by(Pitch.proposal_name)
        
        # template for search results
        return render_template('pitches_search.html', 
                                form=form, 
                                pitches_all=pitches_all,
                                pitches_search=pitches_search, 
                                pitch_count=pitch_count)

    # template for pitchers
    pitch_count = db_session.query(Pitch).count()
    pitches_list = db_session.query(Pitch).filter_by(proposal_name=Pitch.proposal_name).order_by(Pitch.proposal_name)
    return render_template('pitches.html', 
                            form=form,
                            pitches_list=pitches_list,  
                            pitch_count=str(pitch_count))
