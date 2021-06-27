from MyApp import db

class  Course(db.Model):
    __tablename__ = "Course"
    id = db.Column(db.Integer, primary_key=True)
    
    course =db.Column(db.String(36), nullable=False, unique=True)
    

    def __repr__(self):
        return '<Course %r>' % self.username



class  Question(db.Model):
    __tablename__ = "Question"
    id = db.Column(db.Integer, primary_key=True)
    
    question =db.Column(db.String(150), nullable=False, unique=True)
    option_a =db.Column(db.String(100), nullable=False, unique=False)
    option_b =db.Column(db.String(100), nullable=False, unique=False)
    option_c =db.Column(db.String(100), nullable=False, unique=False)
    option_d =db.Column(db.String(100), nullable=False, unique=False)
    correct_option=db.Column(db.String(100), nullable=False, unique=False)
    course_id = db.Column(db.Integer,db.ForeignKey('Course.id'))
    course = db.relationship('Course', backref=db.backref('courses', lazy=True))

    def __repr__(self):
        return '<Question %r>' % self.username

db.create_all()