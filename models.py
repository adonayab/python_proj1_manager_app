from app import db
from hashutils import make_pw_hash
from datetime import datetime

class Message(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(120))
    body = db.Column(db.String(120))
    msg_type = db.Column(db.String(120))
    msg_shift = db.Column(db.String(120))
    owner_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    pub_date = db.Column(db.DateTime)

    def __init__(self, title, body, msg_type, msg_shift, owner, pub_date=None):
        self.title = title
        self.body = body
        self.msg_type = msg_type
        self.msg_shift = msg_shift
        self.owner = owner
        if pub_date is None:
          pub_date = datetime.utcnow()
        self.pub_date = pub_date


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(120))
    email = db.Column(db.String(120), unique=True)
    pw_hash = db.Column(db.String(120))
    messages = db.relationship('Message', backref='owner')

    def __init__(self, name, email, password):
        self.name = name
        self.email = email
        self.pw_hash = make_pw_hash(password)