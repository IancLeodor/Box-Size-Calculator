from flask import Flask
from config import Config
from models import db

app = Flask(__name__)
app.config.from_object(Config)
db.init_app(app)

from routes import *

def create_tables():
    with app.app_context():
        db.create_all()
