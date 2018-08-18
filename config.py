from sqlalchemy import create_engine
import os

# imported by run.py
DEBUG = True
# DATABASE_URL = create_engine('postgres://fotesrlguspefq:a25708e19dbc87dd2f6fb91421acc77fe54f1b9713b4ff028fc828162912a6b8@ec2-54-228-251-254.eu-west-1.compute.amazonaws.com:5432/d1oe01f2fn7o0l', convert_unicode=True)
# SECRET_KEY = '17348hyutrm765'

SECRET_KEY = os.getenv('SECRET_KEY')
DATABASE = os.getenv('DATABASE_URL')

DATABASE_URL = create_engine('DATABASE', convert_unicode=True)
# SECRET_KEY = 'SECRET_KEY'
