import os
from flask import Flask

# not sure if using SQLAlchemy due to sessionmaker (read up on this)
from flask_sqlalchemy import SQLAlchemy

from database import init_db


app = Flask(__name__)

app.config.from_pyfile('config.py')

from models import *

init_db()

from views import *




if __name__ == "__main__":
    app.run(host=os.environ.get('IP'),
    port=int(os.environ.get('PORT')))

