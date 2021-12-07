from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

app.config['SECRET_KEY'] = 'bd97a44f6d3820684ccee22b464dfe61'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///vinay.db'

db = SQLAlchemy(app)

from flask_blog import routes
