from MyApp import app,db,bcrypt
from flask import  Flask,render_template,session,request,url_for,redirect,flash
from .form import AdminRegisterForm,AdminLoginForm
from .models import Admin
from os import environ




@app.route('/Admin Sign in', methods=['POST','GET'])
def AdminRegister():
    form = AdminRegisterForm(request.form)
    if request.method == 'POST' and form.validate():
        hash_password = bcrypt.generate_password_hash(form.password.data)
        admin = Admin(name=form.name.data,username=form.username.data,email=form.email.data,password=hash_password)
        db.session.add(admin)
        db.session.commit()

        flash(f'Welcome {form.username.data} thank you for registering','success')
        return redirect(url_for('AdminPage'))
    
    return render_template('adminH/signin.html',form=form,title="Login page")


@app.route('/admin log in', methods=['POST','GET'])
def AdminLogin():
    form =AdminLoginForm(request.form)
    if request.method == 'POST' and form.validate():
        user = Admin.query.filter_by(email = form.email.data).first()
        if user and bcrypt.check_password_hash(user.password, form.password.data):
            session['email'] = form.email.data
            flash(f'Welcome {form.email.data} You are logged in now ','primary')
            return redirect(request.args.get('next') or url_for('AdminPage'))

        else:
            flash('Wrong email or password', 'danger')
        


    return render_template('adminH/login.html', form=form , title='Admin Log in Page')


@app.route('/Admin home page ')
def AdminPage():
    return render_template('adminH/message.html')