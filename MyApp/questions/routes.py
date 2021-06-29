from MyApp import app,db,bcrypt
from flask import  Flask,render_template,session,request,url_for,redirect,flash
from .form import ExamQuestion,AddCourse
from .models import Course,Question
from os import environ


@app.route('/addcourse', methods=['POST','GET'])
def addcourse():

    form = AddCourse(request.form)

    if request.method =='POST' and form.validate():
        course = Course(course=form.course.data,)
        db.session.add(course)
        db.session.commit()

    return render_template('questions/questions.html', form=form)



@app.route('/AddQuestions')
def AddQuestion():
    form = ExamQuestion(request.form)


    return render_template('questions/questions.html', form=form)
