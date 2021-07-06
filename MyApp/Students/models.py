from flask_sqlalchemy import model
from MyApp import db

class  Student(db.Model):
    __tablename__ = "Student"
    id = db.Column(db.Integer, primary_key=True)
    
    name =db.Column(db.String(30), nullable=False, unique=True)
    username =db.Column(db.String(100), nullable=False, unique=True)
    email = db.Column(db.String(120), nullable=False, unique=True)
    password=db.Column(db.String(120),unique=False, nullable=False)
    

    def __repr__(self):
        return '<Student %r>' % self.username

db.create_all()