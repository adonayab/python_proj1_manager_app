from flask import redirect, render_template, session, flash, request
from models import User, Message
from app import db
from messages.forms import TaskForm
from utils.helpers import badge_general, badge_urgent

from flask import Blueprint

tasks = Blueprint('tasks', __name__)


@tasks.route('/daily-tasks')
def daily_task():
    new_u = True if badge_urgent(
    ) else False  # This is for the urgent note badge
    new_g = True if badge_general(
    ) else False  # This is for the general note badge
    form = TaskForm()

    # mornings = Message.query.order_by(Message.status).filter_by(
    #     category='high').filter_by(shift='Morning').all()
    afternoons = Message.query.order_by(Message.status).filter(
        (Message.category == 'high') | (Message.category == 'low')).filter_by(shift='Afternoon').all()
    evenings = Message.query.order_by(Message.status).filter(
        (Message.category == 'high') | (Message.category == 'low')).filter_by(shift='Evening').all()

    mornings = Message.query.order_by(Message.status).filter(
        (Message.category == 'high') | (Message.category == 'low')).filter_by(shift='Morning').all()

    return render_template('messages/tasks.html',
                           title="Daily Task",
                           mornings=mornings,
                           afternoons=afternoons,
                           evenings=evenings,
                           form=form,
                           new_g=new_g,
                           new_u=new_u)


@tasks.route('/daily-tasks/add', methods=['POST'])
def daily_task_add():

    form = TaskForm()

    if 'email' not in session:
        flash('Login to Add a Task', 'danger')
        return redirect('/login')

    owner = User.query.filter_by(email=session['email']).first()
    if form.validate_on_submit():
        message = Message(title='daily-task',
                          content=form.content.data,
                          category=form.category.data,
                          shift=form.shift.data,
                          owner=owner)
        db.session.add(message)
        db.session.commit()
        flash("Task added Successfully", 'success')
        return redirect('/daily-tasks')

    return render_template('messages/tasks.html', form=form)


@tasks.route('/daily-tasks/', defaults={'id': ''})
@tasks.route('/daily-tasks/<int:id>/delete')
def delete_task(id):

    if 'email' not in session:
        flash('Login to Delete this Note', 'danger')
        return redirect('/login')

    message = Message.query.filter_by(id=id).first()
    db.session.delete(message)
    db.session.commit()
    flash('Task deleted successfully', 'success')
    return redirect('/daily-tasks')


@tasks.route('/daily-tasks/', defaults={'id': ''})
@tasks.route('/daily-tasks/<int:id>/mark')
def mark_task(id):

    if 'email' not in session:
        flash('Login to Mark this Note', 'danger')
        return redirect('/login')

    task = Message.query.filter_by(id=id).first()
    user = User.query.filter_by(email=session['email']).first()

    if task.status == 1:
        task.status = 0
        task.completed_by = ''
        db.session.commit()
        flash(f"Marked not complete", 'warning')
        return redirect('/daily-tasks')
    else:
        task.status = 1
        task.completed_by = user.name
        db.session.commit()
        flash(f"Marked complete", 'success')
        return redirect('/daily-tasks')

    db.session.delete(task)
    db.session.commit()
    flash('Task deleted successfully', 'success')
    return redirect('/daily-tasks')
