from wtforms import Form, StringField , PasswordField , validators,SubmitField,TextField
from wtforms.widgets.core import Option

class ExamQuestion(Form):
    question = TextField('Name:',[validators.Length(min=5, max=20)])
    option_a = TextField('Name:',[validators.Length(min=5, max=20)])
    option_b = TextField('Name:',[validators.Length(min=5, max=20)])
    option_c = TextField('Name:',[validators.Length(min=5, max=20)])
    option_d = TextField('Name:',[validators.Length(min=5, max=20)])
    answer = TextField('Name:',[validators.Length(min=5, max=20)])
    
    


class AddCourse(Form):
    course = StringField('',[validators.Length(min=7, max=36)])
    