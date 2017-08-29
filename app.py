from flask import Flask
from models import db
from admin import admin

app = Flask(__name__)
app.config['SECRET_KEY'] = '123456790'
app.config['MONGODB_SETTINGS'] = {'DB': 'shop'}
db.init_app(app)
admin.init_app(app)
