from flask import request, redirect, render_template, session, flash, Blueprint
from models import User, Message
from app import db
from messages.forms import MessageForm
from utils.helpers import badge_general, badge_urgent, message_query

all_messages = Blueprint('all_messages', __name__)


@all_messages.route('/newpost', methods=['POST'])
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


@all_messages.route('/messages/', defaults={'category': ''})
@all_messages.route('/messages/<category>')
def messages(category):

    new_u = True if badge_urgent() else False  # This is for the urgent note badge
    new_g = True if badge_general() else False  # This is for the general note badge

    form = MessageForm()

    messages = message_query(category.lower())
    return render_template('messages/messages.html',
                           title="Messages",
                           messages=messages,
                           mark="Mark Completed",
                           new_g=new_g,
                           new_u=new_u,
                           form=form)


@all_messages.route('/completed/', defaults={'id': ''})
@all_messages.route('/completed/<int:id>', methods=['Get', 'POST'])
def mark_completion(id):

    new_u = True if badge_urgent() else False  # This is for the urgent note badge
    new_g = True if badge_general() else False  # This is for the general note badge

    form = MessageForm()
    completed_by = ''

    if request.method == 'POST':
        if 'email' not in session:
            flash('Login to Mark this Note', 'danger')
            return redirect('/login')
        message = Message.query.filter_by(id=id).first()
        user = User.query.filter_by(email=session['email']).first()
        if message.status == 1:
            message.status = 0
            message.completed_by = ''
            db.session.commit()
            flash(f"{message.title} unmarked as complete by {user.name}", 'warning')
            return redirect('/completed')
        else:
            message.status = 1
            message.completed_by = user.name
            db.session.commit()
            completed_by = message.completed_by
            flash(f"{message.title} marked complete by {user.name}", 'success')
            return redirect('/messages')

    messages = Message.query.order_by(
        Message.pub_date.desc()).filter(
        Message.category != 'Daily Task').filter_by(status=1).all()
    return render_template('messages/messages.html',
                           title="Completed Messages",
                           messages=messages,
                           mark="Mark Not Completed",
                           completed_by=completed_by,
                           form=form,
                           new_g=new_g,
                           new_u=new_u)
