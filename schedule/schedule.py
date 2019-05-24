from flask import Blueprint, render_template, request, flash, redirect
from app import db
from models import User, UserSchedule
from schedule.forms import ScheduleForm


schedules = Blueprint('schedules', __name__)

current_users_on_schedule = []

@schedules.route('/schedule', methods=['GET', 'POST'])
def schedule():
    form = ScheduleForm()
    users = User.query.all()
    return render_template('schedule.html', users=users, form=form, current_users_on_schedule=current_users_on_schedule)

@schedules.route('/add', methods=['POST'])
def add():
    form = ScheduleForm()
    name = request.form['name']
    start_day = request.form['start_day']
    end_day = request.form['end_day']
    week = str(start_day) + '-' + str(end_day)
    user_schedule = UserSchedule(name=name, week=week)

    if form.validate_on_submit():

        print('In the validation')

        user_schedule.friday = form.start_friday.data + \
            form.start_friday_state.data + '-' + form.end_friday.data + form.end_friday_state.data

        user_schedule.saturday = form.start_saturday.data + \
            form.start_saturday_state.data + '-' + form.end_saturday.data + form.end_saturday_state.data

        user_schedule.sunday = form.start_sunday.data + \
            form.start_sunday_state.data + '-' + form.end_sunday.data + form.end_sunday_state.data

        user_schedule.monday = form.start_monday.data + \
            form.start_monday_state.data + '-' + form.end_monday.data + form.end_monday_state.data

        user_schedule.tuesday = form.start_tuesday.data + \
            form.start_tuesday_state.data + '-' + form.end_tuesday.data + form.end_tuesday_state.data

        user_schedule.wednesday = form.start_wednesday.data + \
            form.start_wednesday_state.data + '-' + form.end_wednesday.data + form.end_wednesday_state.data

        user_schedule.thursday = form.start_thursday.data + \
            form.start_thursday_state.data + '-' + form.end_thursday.data + form.end_thursday_state.data

        db.session.add(user_schedule)
        db.session.commit()
        current_users_on_schedule.append(user_schedule)

        flash(
            f"Schedule for {user_schedule.name} created Successfully", 'success')

        return redirect('/schedule')

    flash('Unsuccessful submit', 'danger')
    return redirect('/schedule')