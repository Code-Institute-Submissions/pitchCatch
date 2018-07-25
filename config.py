from sqlalchemy import create_engine
# imported by run.py
DEBUG = True
DATABASE_URI = create_engine('postgresql://ubuntu:pw123@localhost:5432/pitch_catch_caught', convert_unicode=True)
SECRET_KEY = '17348hyutrm765'