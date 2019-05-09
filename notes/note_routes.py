from flask import request, redirect, render_template, session, flash
from models import User, Message
from app import db
from datetime import datetime
from notes.forms import MessageForm, TaskForm
from utils.helpers import badge_general, badge_urgent, message_query


from flask import Blueprint

notes = Blueprint('notes', __name__)

@notes.route('/newpost', methods=['POST'])
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


@notes.route('/messages/', defaults={'category': ''})
@notes.route('/messages/<category>')
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


@notes.route('/completed/', defaults={'id': ''})
@notes.route('/completed/<int:id>', methods=['Get', 'POST'])
def mark_completion(id):

    new_u = True if badge_urgent() else False  # This is for the urgent note badge
    new_g = True if badge_general() else False  # This is for the general note badge

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


@notes.route('/messages/', defaults={'id': ''})
@notes.route('/single/<int:id>', methods=['GET'])
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


@notes.route('/messages/', defaults={'id': ''})
@notes.route('/single/<int:id>/delete', methods=['POST'])
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


@notes.route('/messages/', defaults={'id': ''})
@notes.route('/single/<int:id>/edit', methods=['POST'])
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


