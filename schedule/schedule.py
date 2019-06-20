from flask import Blueprint, render_template, request, flash, redirect
from app import db
from models import User, UserSchedule, WeekSchedule

schedules = Blueprint('schedules', __name__)


@schedules.route('/schedule', methods=['GET', 'POST'])
def schedule():
    all_schedules = WeekSchedule.query.all()

    if request.method == 'POST':
        start_day = request.form['start_day']
        end_day = request.form['end_day']

        if not start_day and not end_day:
            flash("Select start day and end day", 'danger')
            return render_template('/schedules/index.html', title='Schedules', all_schedules=all_schedules)
        if not start_day:
            flash("Select the start day", 'danger')
            return render_template('/schedules/index.html', title='Schedules', all_schedules=all_schedules)

        if not end_day:
            flash("Select the end day", 'danger')
            return render_template('/schedules/index.html', title='Schedules', all_schedules=all_schedules)

        week = str(start_day).replace('-', '/') + \
               ' to ' + str(end_day).replace('-', '/')
        current_week_schedule = WeekSchedule(on_week = week)
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

    if request.method == 'POST':

        week_id = id
        current_week = WeekSchedule.query.filter_by(id=week_id).first()

        name = request.form['name']
        user_schedule = UserSchedule(name=name, week=current_week)

        fri_start = request.form['fri_start']
        fri_start_state = request.form['fri_start_state']
        fri_end = request.form['fri_end']
        fri_end_state = request.form['fri_end_state']

        sat_start = request.form['sat_start']
        sat_start_state = request.form['sat_start_state']
        sat_end = request.form['sat_end']
        sat_end_state = request.form['sat_end_state']

        sun_start = request.form['sun_start']
        sun_start_state = request.form['sun_start_state']
        sun_end = request.form['sun_end']
        sun_end_state = request.form['sun_end_state']

        mon_start = request.form['mon_start']
        mon_start_state = request.form['mon_start_state']
        mon_end = request.form['mon_end']
        mon_end_state = request.form['mon_end_state']

        tue_start = request.form['tue_start']
        tue_start_state = request.form['tue_start_state']
        tue_end = request.form['tue_end']
        tue_end_state = request.form['tue_end_state']

        wed_start = request.form['wed_start']
        wed_start_state = request.form['wed_start_state']
        wed_end = request.form['wed_end']
        wed_end_state = request.form['wed_end_state']

        thu_start = request.form['thu_start']
        thu_start_state = request.form['thu_start_state']
        thu_end = request.form['thu_end']
        thu_end_state = request.form['thu_end_state']

        if sat_start == 'OFF' and sat_start_state == 'OFF' and sat_end == 'OFF' and sat_end_state == 'OFF':
            user_schedule.saturday = 'OFF'
        else:
            user_schedule.saturday = sat_start + \
                                     sat_start_state + ' - ' + sat_end + sat_end_state

        if sun_start == 'OFF' and sun_start_state == 'OFF' and sun_end == 'OFF' and sun_end_state == 'OFF':
            user_schedule.sunday = 'OFF'
        else:
            user_schedule.sunday = sun_start + \
                                   sun_start_state + ' - ' + sun_end + sun_end_state

        if mon_start == 'OFF' and mon_start_state == 'OFF' and mon_end == 'OFF' and mon_end_state == 'OFF':
            user_schedule.monday = 'OFF'
        else:
            user_schedule.monday = mon_start + \
                                   mon_start_state + ' - ' + mon_end + mon_end_state

        if tue_start == 'OFF' and tue_start_state == 'OFF' and tue_end == 'OFF' and tue_end_state == 'OFF':
            user_schedule.tuesday = 'OFF'
        else:
            user_schedule.tuesday = tue_start + \
                                    tue_start_state + ' - ' + tue_end + tue_end_state

        if wed_start == 'OFF' and wed_start_state == 'OFF' and wed_end == 'OFF' and wed_end_state == 'OFF':
            user_schedule.wednesday = 'OFF'
        else:
            user_schedule.wednesday = wed_start + \
                                      wed_start_state + ' - ' + wed_end + wed_end_state

        if thu_start == 'OFF' and thu_start_state == 'OFF' and thu_end == 'OFF' and thu_end_state == 'OFF':
            user_schedule.thursday = 'OFF'
        else:
            user_schedule.thursday = thu_start + \
                                     thu_start_state + ' - ' + thu_end + thu_end_state

        if fri_start == 'OFF' and fri_start_state == 'OFF' and fri_end == 'OFF' and fri_end_state == 'OFF':
            user_schedule.friday = 'OFF'
        else:
            user_schedule.friday = fri_start + \
                                   fri_start_state + ' - ' + fri_end + fri_end_state

        db.session.add(user_schedule)
        db.session.commit()

        flash(
            f"Schedule for {user_schedule.name} created Successfully", 'success')

        # When editing a user schedule this block deletes the old user from the database
        if 'old_id' in request.form:
            old_id = request.form['old_id']
            user_schedule = UserSchedule.query.filter_by(id=old_id).first()
            db.session.delete(user_schedule)
            db.session.commit()

        return redirect(f'/schedule/add/{week_id}')

    return render_template('schedules/add.html', title='Create Schedules' ,users=users, current_schedule=current_schedule, week_id=id)


@schedules.route('/schedule/view')
def view():
    week_id = request.args.get('week_id')

    view_schedule = WeekSchedule.query.filter_by(
        id=week_id).order_by(WeekSchedule.id.desc()).first()
    all_schedules = WeekSchedule.query.all()

    return render_template('schedules/index.html', title='View Schedules', view_schedule=view_schedule, all_schedules=all_schedules)


@schedules.route('/schedule/edit/<id>')
def edit(id):
    user_schedule = UserSchedule.query.filter_by(id=id).first()
    users = User.query.all()

    return render_template('schedules/edit.html', title='Edit Schedules', user_schedule=user_schedule, users=users)


@schedules.route('/schedule/delete/<id>')
def delete(id):
    user_schedule = UserSchedule.query.filter_by(id=id).first()
    name = user_schedule.name
    week_id = user_schedule.week_id
    db.session.delete(user_schedule)
    db.session.commit()
    flash(f"Schedule for {name} deleted Successfully", 'danger')
    return redirect(f'/schedule/add/{week_id}')
