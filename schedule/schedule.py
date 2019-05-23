from flask import Blueprint, render_template, request, flash, redirect
from app import db
from models import User, UserSchedule
from schedule.forms import ScheduleForm


schedules = Blueprint('schedules', __name__)


@schedules.route('/schedule', methods=['GET', 'POST'])
def schedule():

    current_users_on_schedule = []
    form = ScheduleForm()
    users = User.query.all()

    if request.method == 'POST':
        name = request.form['name']
        start_day = request.form['start_day']
        end_day = request.form['end_day']
        week = str(start_day) + '-' + str(end_day)
        if form.validate_on_submit():
            user_schedule = UserSchedule(name=name, week=week)

            user_schedule.friday = form.start_friday.data + \
                form.start_friday_state + '-' + form.end_friday + form.end_friday_state

            user_schedule.saturday = form.start_saturday.data + \
                form.start_saturday_state + '-' + form.end_saturday + form.end_saturday_state

            user_schedule.sunday = form.start_sunday.data + \
                form.start_sunday_state + '-' + form.end_sunday + form.end_sunday_state

            user_schedule.monday = form.start_monday.data + \
                form.start_monday_state + '-' + form.end_monday + form.end_monday_state

            user_schedule.tuesday = form.start_tuesday.data + \
                form.start_tuesday_state + '-' + form.end_tuesday + form.end_tuesday_state

            user_schedule.wednesday = form.start_wednesday.data + \
                form.start_wednesday_state + '-' + form.end_wednesday + form.end_wednesday_state

            user_schedule.thursday = form.start_thursday.data + \
                form.start_thursday_state + '-' + form.end_thursday + form.end_thursday_state

            db.session.add(user_schedule)
            db.session.commit()
            current_users_on_schedule.append(user_schedule)

            flash(
                f"Schedule for {user_schedule.name} created Successfully", 'success')

            return redirect('/schedule')

    return render_template('schedule.html', users=users, form=form, current_users_on_schedule=current_users_on_schedule)
