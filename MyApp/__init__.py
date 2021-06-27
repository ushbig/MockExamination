from flask import Flask ,redirect,render_template 
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
app = Flask(__name__)
app.secret_key = '\xaeb\x87\xb0|\xb0\xbf+\tn\x8dH\xea3\xa7t/\x1d\xdfT\x19\x1b7\xea'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///MockExam.db'

db =SQLAlchemy(app)

bcrypt = Bcrypt(app)
from MyApp.AdminP import routes 
from MyApp.Students import routes
from MyApp.questions import routes
