from flask_sqlalchemy import SQLAlchemy
from models import User, Message

def badge_urgent():
    urgent_messages = Message.query.filter_by(
        category='Urgent').filter_by(status=0).all()
    if urgent_messages:
        return True

def badge_general():
    general_messages = Message.query.filter_by(
        category='General').filter_by(status=0).all()
    if general_messages:
        return True