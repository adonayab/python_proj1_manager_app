from flask import Blueprint, render_template

schedules = Blueprint('schedules', __name__)

@schedules.route('/schedule')
def schedule():
  return render_template('schedule.html')