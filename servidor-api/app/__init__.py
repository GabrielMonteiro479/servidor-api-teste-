import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

def create_app(enviroment):
    app = Flask(__name__)
    app.config.from_pyfile('../config/%s.cfg' % enviroment)
    return app

def create_db(application):
    return SQLAlchemy(application)

env = os.getenv('ENV') or 'dev'

app = create_app(env)
db = create_db(app)
