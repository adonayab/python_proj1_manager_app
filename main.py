from flask import Flask, request, redirect, render_template, session, flash
from flask_sqlalchemy import SQLAlchemy
from models import User, Message
from app import app, db
from hashutils import check_pw_hash
from datetime import datetime
from forms import RegistrationForm, LoginForm, MessageForm, TaskForm
from helpers import badge_general, badge_urgent, message_query

# @app.before_request
# def require_login():
#     allowed_routes = ['login', 'signup', 'index', 'message']
#     if request.endpoint not in allowed_routes and 'email' not in session and '/static/' not in request.path:
#         return redirect('/login')


@app.route("/logout", methods=['POST'])
def logout():
    del session['email']
    return redirect('/login')


@app.route('/login', methods=['POST', 'GET'])
def login():
    if 'email' in session:
        return redirect('/messages')
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        if user and check_pw_hash(form.password.data, user.pw_hash):
            session['email'] = user.email
            return redirect('/messages')
        else:
            flash('Login Unsuccessful. Please check email and password',
                  'danger')
    return render_template('login.html', title='Message Login', form=form)


@app.route('/signup', methods=['POST', 'GET'])
def signup():
    if 'email' in session:
        return redirect('/messages')
    form = RegistrationForm()
    if form.validate_on_submit():
        user = User(name=form.name.data,
                    email=form.email.data,
                    password=form.password.data)
        db.session.add(user)
        db.session.commit()
        flash(f'Account created for {form.name.data}', 'success')
        return redirect('/login')

    return render_template('signup.html', title='Messagez Signup', form=form)


@app.route('/newpost', methods=['POST'])
def newpost():

    if 'email' not in session:
        flash('Login to Leave a Note', 'danger')
        return redirect('/login')

    form = MessageForm()
    owner = User.query.filter_by(email=session['email']).first()
    if form.validate_on_submit():
        message = Message(title=form.title.data,
                          content=form.content.data,
                          category=form.category.data,
                          shift=form.shift.data,
                          owner=owner)
        db.session.add(message)
        db.session.commit()
        flash("Posted Note Successfully", 'success')
        return redirect('/messages')


@app.route('/messages/', defaults={'category': ''})
@app.route('/messages/<category>')
def messages(category):
    
    new_u = True if badge_urgent(
    ) else False  # This is for the urgent note badge
    new_g = True if badge_general(
    ) else False  # This is for the general note badge
    
    form = MessageForm()

    messages = message_query(category.lower())
    return render_template('messages.html',
                            title="Messages",
                            messages=messages,
                            mark="Mark Completed",
                            new_g=new_g,
                            new_u=new_u,
                            form=form)


@app.route('/completed/', defaults={'id': ''})
@app.route('/completed/<int:id>', methods=['Get', 'POST'])
def mark_completion(id):

    new_u = True if badge_urgent(
    ) else False  # This is for the urgent note badge
    new_g = True if badge_general(
    ) else False  # This is for the general note badge

    form = MessageForm()
    completed_by = ''

    if request.method == 'POST':
        message = Message.query.filter_by(id=id).first()
        user = User.query.filter_by(email=session['email']).first()
        if 'email' not in session:
            flash('Login to Mark this Note', 'danger')
            return redirect('/login')
        if message.status == 1:
            message.status = 0
            message.completed_by = ''
            db.session.commit()
            return redirect('/completed')
        else:
            message.status = 1
            message.completed_by = user.name
            db.session.commit()
            completed_by = message.completed_by
            return redirect('/completed')

    messages = Message.query.order_by(
        Message.pub_date.desc()).filter_by(status=1).all()
    return render_template('messages.html',
                           title="Completed Messages",
                           messages=messages,
                           mark="Unmark Completed",
                           completed_by=completed_by,
                           form=form,
                           new_g=new_g,
                           new_u=new_u)


@app.route('/messages/', defaults={'id': ''})
@app.route('/single/<int:id>', methods=['GET'])
def single(id):
    new_u = True if badge_urgent(
    ) else False  # This is for the urgent note badge
    new_g = True if badge_general(
    ) else False  # This is for the general note badge
    message = Message.query.filter_by(id=id).first()

    form = MessageForm()
    form.title.data = message.title
    form.category.data = message.category
    form.shift.data = message.shift
    form.content.data = message.content

    return render_template('single.html',
                           title=message.title,
                           message=message,
                           form=form,
                           new_g=new_g,
                           new_u=new_u)


@app.route('/messages/', defaults={'id': ''})
@app.route('/single/<int:id>/delete', methods=['POST'])
def delete_single(id):

    if 'email' not in session:
        flash('Login to Modify this Note', 'danger')
        return redirect('/login')

    message = Message.query.filter_by(id=id).first()
    if message.owner.email != session['email']:
        flash('Unauthorised to Delete this Note', 'danger')
        return redirect(f'/single/{message.id}')

    db.session.delete(message)
    db.session.commit()
    flash('Note deleted successfully', 'success')
    return redirect('/messages')


@app.route('/messages/', defaults={'id': ''})
@app.route('/single/<int:id>/edit', methods=['POST'])
def edit_single(id):

    message = Message.query.filter_by(id=id).first()
    form = MessageForm()
    if 'email' not in session:
        flash('Login to Modify this Note', 'danger')
        return redirect('/login')

    if message.owner.email != session['email']:
        flash('Unauthorised to Edit this Note', 'danger')
        return redirect(f'/single/{message.id}')

    if form.validate_on_submit():
        message.title = form.title.data
        message.content = form.content.data
        message.category = form.category.data
        message.shift = form.shift.data
        message.pub_date = datetime.utcnow()
        message.status = 0
        db.session.commit()
        flash('Successfully updated note', 'success')
        return redirect('/messages')

    return render_template('edit.html',
                           title="Edit",
                           form=form,
                           message=message)


@app.route('/daily-tasks')
def daily_task():
    new_u = True if badge_urgent(
    ) else False  # This is for the urgent note badge
    new_g = True if badge_general(
    ) else False  # This is for the general note badge
    form = TaskForm()

    mornings = Message.query.order_by(Message.pub_date.desc()).filter_by(
        category='Daily Task').filter_by(shift='Morning').all()
    afternoons = Message.query.order_by(Message.pub_date.desc()).filter_by(
        category='Daily Task').filter_by(shift='Afternoon').all()
    evenings = Message.query.order_by(Message.pub_date.desc()).filter_by(
        category='Daily Task').filter_by(shift='Evening').all()

    return render_template('tasks.html',
                           title="Daily Task",
                           mornings=mornings,
                           afternoons=afternoons,
                           evenings=evenings,
                           form=form,
                           new_g=new_g,
                           new_u=new_u)


@app.route('/daily-tasks/add', methods=['POST'])
def daily_task_add():

    form = TaskForm()

    if 'email' not in session:
        flash('Login to Add a Task', 'danger')
        return redirect('/login')

    owner = User.query.filter_by(email=session['email']).first()
    if form.validate_on_submit():
        message = Message(title='daily-task',
                          content=form.content.data,
                          category='Daily Task',
                          shift=form.shift.data,
                          owner=owner)
        db.session.add(message)
        db.session.commit()
        flash("Task added Successfully", 'success')
        return redirect('/daily-tasks')

    return render_template('tasks.html', form=form)


@app.route('/daily-tasks-delete')
def modify_daily_task():
    new_u = True if badge_urgent(
    ) else False  # This is for the urgent note badge
    new_g = True if badge_general(
    ) else False  # This is for the general note badge
    form = TaskForm()

    mornings = Message.query.order_by(Message.pub_date.desc()).filter_by(
        category='Daily Task').filter_by(shift='Morning').all()
    afternoons = Message.query.order_by(Message.pub_date.desc()).filter_by(
        category='Daily Task').filter_by(shift='Afternoon').all()
    evenings = Message.query.order_by(Message.pub_date.desc()).filter_by(
        category='Daily Task').filter_by(shift='Evening').all()

    return render_template('task-delete.html',
                           title="Daily Task",
                           mornings=mornings,
                           afternoons=afternoons,
                           evenings=evenings,
                           form=form,
                           new_g=new_g,
                           new_u=new_u)


@app.route('/daily-tasks/', defaults={'id': ''})
@app.route('/daily-tasks-delete/<int:id>/delete', methods=['POST'])
def delete_task(id):

    if 'email' not in session:
        flash('Login to Modify this Note', 'danger')
        return redirect('/login')

    message = Message.query.filter_by(id=id).first()
    db.session.delete(message)
    db.session.commit()
    flash('Task deleted successfully', 'success')
    return redirect('/daily-tasks-delete')


if __name__ == "__main__":
    app.run()
