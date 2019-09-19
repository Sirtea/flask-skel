from flask import Flask
from models import db
from admin import admin
import os

SECRET_KEY = os.environ.get('SECRET_KEY')
MONGODB_URL = os.environ.get('MONGODB_URL')

app = Flask(__name__)
app.config['SECRET_KEY'] = SECRET_KEY
app.config['MONGODB_SETTINGS'] = {'host': MONGODB_URL}
db.init_app(app)
admin.init_app(app)
