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