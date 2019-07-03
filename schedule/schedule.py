from datetime import timedelta

from flask import Blueprint, render_template, request, flash, redirect, session, make_response, url_for
from app import db
from models import User, UserSchedule, WeekSchedule, DaysOfSchedule
import pdfkit
from utils.helpers import get_date, days_generator

schedules = Blueprint('schedules', __name__)


@schedules.route('/schedule', methods=['GET', 'POST'])
def schedule():
    all_schedules = WeekSchedule.query.order_by(WeekSchedule.start_date.desc()).all()

    if request.method == 'POST':

        if 'email' not in session:
            flash('Login as Admin to create a schedule', 'danger')
            return redirect('/login')

        owner = User.query.filter_by(email=session['email']).first()
        if not owner.admin:
            flash("Log in as Admin to create a schedule", 'danger')
            return redirect('/schedule')

        start_day = request.form['start_day']

        if not start_day:
            flash("Select the start day", 'danger')
            return render_template('/schedules/index.html', title='Schedules', all_schedules=all_schedules)

        start_date = get_date(start_day)
        end_date = start_date + timedelta(days=6)
        week = start_date.strftime('%A %d, %Y') + ' to ' + end_date.strftime('%A %d, %Y')
        current_week_schedule = WeekSchedule(start_date=start_date, end_date=end_date)
        db.session.add(current_week_schedule)
        db.session.commit()
        flash(
            f"Add users to schedule for {week}", 'success')

        return redirect(f'/schedule/add/{current_week_schedule.id}')

    return render_template('/schedules/index.html', title='Schedules', all_schedules=all_schedules)


@schedules.route('/schedule', defaults={'id': ''})
@schedules.route('/schedule/add/<id>', methods=['GET', 'POST'])
def add(id):
    users = User.query.all()
    current_schedule = WeekSchedule.query.filter_by(id=id).first()

    start_day  = current_schedule.start_date.strftime("%A")
    # Generates days starting from the schedule day
    days_of_week = days_generator(start_day)

    if request.method == 'POST':

        if 'email' not in session:
            flash('Login as Admin to create user schedules', 'danger')
            return redirect('/login')

        owner = User.query.filter_by(email=session['email']).first()
        if not owner.admin:
            flash("Login as Admin to create user schedules", 'danger')
            return redirect('/schedule')

        name = request.form['name']
        user_schedule = UserSchedule(name=name, week=current_schedule)

        for day in days_of_week:
            tim_in = request.form[f'{day}_start'] + ' ' + request.form[f'{day}_start_state']
            tim_out = request.form[f'{day}_end'] + ' ' + request.form[f'{day}_end_state']
            if 'OFF' in tim_in:
                tim_in = 'OFF'
            if 'OFF' in tim_out:
                tim_out = 'OFF'
            db.session.add(DaysOfSchedule(day=day, usr_sch=user_schedule, tim_in=tim_in, tim_out=tim_out))

        db.session.add(user_schedule)
        db.session.commit()

        flash(
            f"Schedule for {user_schedule.name} created Successfully", 'success')

        return redirect(f'/schedule/add/{id}')

    return render_template('schedules/add.html', title='Create Schedules', users=users,
                           current_schedule=current_schedule, week_id=id, days_of_week=days_of_week)


@schedules.route('/schedule/view')
def view():
    if 'email' not in session:
        flash('Login to View a schedule', 'danger')
        return redirect('/login')

    week_id = request.args.get('week_id')

    view_schedule = WeekSchedule.query.filter_by(
        id=week_id).first()

    start_day = view_schedule.week_schedule[0].user_schedule[0].day
    days_of_week = days_generator(start_day)

    all_schedules = WeekSchedule.query.order_by(WeekSchedule.start_date.desc()).all()

    return render_template('schedules/index.html', title='View Schedules', view_schedule=view_schedule,
                           all_schedules=all_schedules, days_of_week=days_of_week)


@schedules.route('/schedule/edit/<id>', methods=['GET','POST'])
def edit(id):
    if 'email' not in session:
        flash('Login as Admin to Edit a schedule', 'danger')
        return redirect('/login')

    owner = User.query.filter_by(email=session['email']).first()
    if not owner.admin:
        flash("Login as Admin to Edit a schedule", 'danger')
        return redirect('/schedule')

    user_schedule = UserSchedule.query.filter_by(id=id).first()
    start_day = user_schedule.user_schedule[0].day
    days_of_week = days_generator(start_day)

    if request.method == 'POST':
        for day in days_of_week:
            tim_in = request.form[f'{day}_start'] + ' ' + request.form[f'{day}_start_state']
            tim_out = request.form[f'{day}_end'] + ' ' + request.form[f'{day}_end_state']
            if 'OFF' in tim_in:
                tim_in = 'OFF'
            if 'OFF' in tim_out:
                tim_out = 'OFF'
            day = DaysOfSchedule.query.filter_by(day=day).filter_by(usr_sch_id=user_schedule.id).first()
            day.tim_in = tim_in
            day.tim_out = tim_out
            db.session.add(day)

        db.session.add(user_schedule)
        db.session.commit()
        flash("Successfully Updated Schedule", 'success')
        return redirect(f'/schedule/add/{user_schedule.week_id}')

    return render_template('schedules/edit.html', title='Edit Schedules', user_schedule=user_schedule, days_of_week=days_of_week)


@schedules.route('/schedule/delete/<id>')
def delete(id):
    if 'email' not in session:
        flash('Login as Admin to Delete a schedule', 'danger')
        return redirect('/login')

    owner = User.query.filter_by(email=session['email']).first()
    if not owner.admin:
        flash("Login as Admin to Delete a schedule", 'danger')
        return redirect('/schedule')

    user_schedule = UserSchedule.query.filter_by(id=id).first()
    days_of_sche = DaysOfSchedule.query.filter_by(usr_sch_id=user_schedule.id).all()
    name = user_schedule.name
    week_id = user_schedule.week_id
    for day in days_of_sche:
        db.session.delete(day)
    db.session.delete(user_schedule)
    db.session.commit()
    flash(f"Schedule for {name} deleted Successfully", 'danger')
    return redirect(f'/schedule/add/{week_id}')


@schedules.route('/schedule/pdf/<id>')
def to_pdf(id):

    schedule = WeekSchedule.query.filter_by(id=id).first()
    start_day = schedule.week_schedule[0].user_schedule[0].day
    days_of_week = days_generator(start_day)

    rendered = render_template('schedules/pdf-view.html', schedule=schedule, days_of_week=days_of_week)
    css = ['static/css/bootstrap-material.css']
    pdf = pdfkit.from_string(rendered, False, css=css)

    response = make_response(pdf)
    response.headers['Content-Type'] = 'application/pdf'
    response.headers['Content-Disposition'] = 'inline; filename=schedule.pdf'

    return response
