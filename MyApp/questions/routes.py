from MyApp import app,db,bcrypt
from flask import  Flask,render_template,session,request,url_for,redirect,flash
from .form import ExamQuestion,AddCourse
from .models import Course,Question
from os import environ


@app.route('/addcourse', methods=['POST','GET'])
def addcourse():

    form = AddCourse(request.form)

    if request.method =='POST' and form.validate():
        cours = Course(cours=form.course.data)
        db.session.add(cours)
        db.session.commit()

    return render_template('questions/questions.html', form=form)



@app.route('/examQuestion', methods=["POST","GET"])
def examQuestion():
    form = ExamQuestion()
    if request.method =='POST' and form.validate():
        cour = Question(cours=form.cour.data)
        db.session.add(cour)
        db.session.commit()
    

    return render_template('questions/questions.html', form=form)
