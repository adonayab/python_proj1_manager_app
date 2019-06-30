from app import db
from utils.hashutils import make_pw_hash
from datetime import datetime


class Message(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(120), nullable=False)
    content = db.Column(db.Text, nullable=False)
    category = db.Column(db.String(120), nullable=False)
    shift = db.Column(db.String(120), nullable=False)
    status = db.Column(db.Boolean, default=False, nullable=False)
    owner_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    pub_date = db.Column(db.DateTime, default=datetime.utcnow, nullable=False)
    completed_by = db.Column(db.String(120))

    def __init__(self, title, content, category, shift, owner):
        self.title = title
        self.content = content
        self.category = category
        self.shift = shift
        self.owner = owner


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(120), nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    pw_hash = db.Column(db.String(120), nullable=False)
    admin = db.Column(db.Boolean, default=False, nullable=False)
    messages = db.relationship('Message', backref='owner', lazy=True)

    def __init__(self, name, email, password):
        self.name = name
        self.email = email
        self.pw_hash = make_pw_hash(password)


class DaysOfSchedule(db.Model):

    id = db.Column(db.Integer, primary_key=True)
    day = db.Column(db.String(120), nullable=False)
    tim_in = db.Column(db.String(120))
    tim_out = db.Column(db.String(120))
    usr_sch_id = db.Column(db.Integer, db.ForeignKey('user_schedule.id'),
                        nullable=False)

    def __init__(self, day, usr_sch, tim_in, tim_out):
        self.day = day
        self.usr_sch = usr_sch
        self.tim_in = tim_in
        self.tim_out = tim_out


class UserSchedule(db.Model):

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(120), nullable=False)
    user_schedule = db.relationship('DaysOfSchedule', backref='usr_sch', lazy=True)
    week_id = db.Column(db.Integer, db.ForeignKey('week_schedule.id'),
                        nullable=False)

    def __init__(self, name, week):
        self.name = name
        self.week = week


class WeekSchedule(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    start_date = db.Column(db.DateTime, nullable=False)
    end_date = db.Column(db.DateTime, nullable=False)
    week_schedule = db.relationship('UserSchedule', backref='week', lazy=True)

    def __init__(self, start_date, end_date):
        self.start_date = start_date
        self.end_date = end_date


class Food(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(120), nullable=False, unique=True)
    cook_time = db.Column(db.Integer, nullable=False)
    exp_time = db.Column(db.Integer, nullable=False, default=4)

    def __init__(self, name, cook_time):
        self.name = name
        self.cook_time = cook_time
