from MyApp.questions import models
from flask_sqlalchemy import model
from MyApp import app,db,bcrypt
from flask import  Flask,render_template,session,request,url_for,redirect,flash
from .form import StudentRegisterForm,StudentLoginForm
from .models import Student
from MyApp.questions import models 
from os import environ



@app.route('/')
def home():
    return redirect(url_for('StudentLogin'))

@app.route('/Sign in', methods=['POST','GET'])
def StudentRegister():
    form = StudentRegisterForm(request.form)
    if request.method == 'POST' and form.validate():
        hash_password = bcrypt.generate_password_hash(form.password.data)
        student = Student(name=form.name.data,username=form.username.data,email=form.email.data,password=hash_password)
        db.session.add(student)
        db.session.commit()

        flash(f'Welcome {form.username.data} thank you for registering','success')
        return redirect(url_for('StudentPage'))
    
    return render_template('student/signin.html',form=form,title="Login page")


@app.route('/log in', methods=['POST','GET'])
def StudentLogin():
    form =StudentLoginForm(request.form)
    if request.method == 'POST' and form.validate():
        student = Student.query.filter_by(email = form.email.data).first()
        if student and bcrypt.check_password_hash(student.password, form.password.data):
            session['email'] = form.email.data
            flash(f'Welcome {form.email.data} You are logged in now ','primary')
            return redirect(request.args.get('next') or url_for('StudentPage'))

        else:
            flash('Wrong email or password', 'danger')
        


    return render_template('student/login.html', form=form , title='Student Log in Page')


@app.route('/Student home page ')
def StudentPage():
    message = session['email']
    selection = models.Course.query.all()
    return render_template('student/studentHomePage.html' , message=message , selection=selection)


@app.route('/QuestionPage')
def questionPage():
    
    return render_template('student')