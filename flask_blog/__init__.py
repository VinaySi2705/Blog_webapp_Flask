from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager
from flask_mail import Mail
import os


app = Flask(__name__)

app.config['SECRET_KEY'] = 'bd97a44f6d3820684ccee22b464dfe61'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///vinay.db'

db = SQLAlchemy(app)
bcrypt = Bcrypt(app)
login_manager = LoginManager(app)
login_manager.login_view = 'users.login'
login_manager.login_message_category = 'info'
app.config['MAIL_SERVER'] = 'smtp.googlemail.com'
app.config['MAIL_PORT'] = 587
app.config['MAIL_USE_TLS'] = True
app.config['MAIL_USERNAME'] = os.environ.get('EMAIL_USER')
app.config['MAIL_PASSWORD'] = os.environ.get('EMAIL_PASS')
mail = Mail(app)


from flask_blog.users.routes import users
from flask_blog.posts.routes import posts
from flask_blog.main.routes import main
from flask_blog.errors.handlers import errors

app.register_blueprint(errors)
app.register_blueprint(users)
app.register_blueprint(posts)
app.register_blueprint(main)
