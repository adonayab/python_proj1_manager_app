from flask import redirect, render_template, session, flash
from models import Message
from main import db
from datetime import datetime
from messages.forms import MessageForm
from utils.helpers import badge_general, badge_urgent


from flask import Blueprint

single_messages = Blueprint('single_messages', __name__)

@single_messages.route('/messages/', defaults={'id': ''})
@single_messages.route('/single/<int:id>', methods=['GET'])
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


@single_messages.route('/messages/', defaults={'id': ''})
@single_messages.route('/single/<int:id>/delete', methods=['POST'])
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


@single_messages.route('/messages/', defaults={'id': ''})
@single_messages.route('/single/<int:id>/edit', methods=['POST'])
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


