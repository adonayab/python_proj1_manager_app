from flask import Blueprint, render_template
from app import db
from models import User
schedules = Blueprint('schedules', __name__)


@schedules.route('/schedule')
def schedule():
    users = User.query.all()
    return render_template('schedule.html', users=users)
