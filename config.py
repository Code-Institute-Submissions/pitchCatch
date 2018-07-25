from sqlalchemy import create_engine
# imported by run.py
DEBUG = True
# DATABASE_URL = create_engine('postgresql://ubuntu:pw123@localhost:5432/pitch_catch_caught', convert_unicode=True)
DATABASE_URL = create_engine('postgres://fotesrlguspefq:a25708e19dbc87dd2f6fb91421acc77fe54f1b9713b4ff028fc828162912a6b8@ec2-54-228-251-254.eu-west-1.compute.amazonaws.com:5432/d1oe01f2fn7o0l', convert_unicode=True)
SECRET_KEY = '17348hyutrm765'