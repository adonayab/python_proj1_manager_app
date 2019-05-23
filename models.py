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


class UserSchedule(db.Model):

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(120), nullable=False)
    week = db.Column(db.String(120), nullable=False)
    monday = db.Column(db.String(120))
    tuesday = db.Column(db.String(120))
    wednesday = db.Column(db.String(120))
    thursday = db.Column(db.String(120))
    friday = db.Column(db.String(120))
    saturday = db.Column(db.String(120))
    sunday = db.Column(db.String(120))

    def __init__(self, name, week):
        self.name = name
        self.week = week
