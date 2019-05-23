from flask import Blueprint, render_template
from models import User
from schedule.forms import ScheduleForm


schedules = Blueprint('schedules', __name__)

@schedules.route('/schedule')
def schedule():
    scheduleForm = ScheduleForm
    users = User.query.all()
    return render_template('schedule.html', users=users, scheduleForm=scheduleForm)
