from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager
app = Flask(__name__)

app.config['SECRET_KEY'] = 'bd97a44f6d3820684ccee22b464dfe61'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///vinay.db'

db = SQLAlchemy(app)
bcrypt = Bcrypt(app)
login_manager = LoginManager(app)


from flask_blog import routes
