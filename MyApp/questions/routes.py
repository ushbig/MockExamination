from MyApp import app,db,bcrypt
from flask import  Flask,render_template,session,request,url_for,redirect,flash
from .form import ExamQuestion,AddCourse
from .models import Course,Question
from os import environ


@app.route('/Add Course', methods=['POST','GET'])
def addCourse():

    form = AddCourse(request.form)

    if request.method =='POST':
        course = Course(course=form.course.data,)
        db.session.add(course)
        db.session.commit()

    return render_template('questions/questions.html', form=form)



@app.route('/Add Questions')
def AddQuestion():


    return render_template('questions/questions.html')
