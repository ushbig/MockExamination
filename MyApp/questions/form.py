from wtforms import Form, StringField , PasswordField , validators,SubmitField,TextField,TextAreaField
from wtforms.widgets.core import Option

class ExamQuestion(Form):
    question = TextAreaField('Question:',[validators.Length(min=5, max=700)])
    option_a = TextField('Option A:',[validators.Length(min=2, max=70)])
    option_b = TextField('Option B:',[validators.Length(min=2, max=70)])
    option_c = TextField('Option C:',[validators.Length(min=2, max=70)])
    option_d = TextField('Option D:',[validators.Length(min=2, max=70)])
    answer = TextField('Answer:',[validators.Length(min=1, max=20)])
    
    


class AddCourse(Form):
    course = StringField('',[validators.Length(36)])
    