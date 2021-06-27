from wtforms import Form, StringField , PasswordField , validators,SubmitField

class StudentRegisterForm(Form):
    name = StringField('Name:',[validators.Length(min=5, max=20)])
    username = StringField('Username:',[validators.Length(min=5, max=20)])
    email = StringField('Email:',[validators.Length(min=7, max=36)])
    password = PasswordField('Password:',[validators.EqualTo
    ('confirm',message='Both password must match!')])
    confirm = PasswordField('Repeat password:',)


class StudentLoginForm(Form):
    email = StringField('Email:',[validators.Length(min=7, max=36)])
    password = PasswordField('Password:')