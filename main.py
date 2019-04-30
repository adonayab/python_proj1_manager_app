from flask import Flask, request, redirect, render_template, session, flash
from flask_sqlalchemy import SQLAlchemy
from models import User, Message
from app import app, db
from hashutils import check_pw_hash
from datetime import datetime
from forms import RegistrationForm, LoginForm, MessageForm

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
            flash('Login Unsuccessful. Please check email and password', 'danger')
    return render_template('login.html', title='Message Login', form=form)


@app.route('/signup', methods=['POST', 'GET'])
def signup():
    if 'email' in session:
        return redirect('/messages')
    form = RegistrationForm()
    if form.validate_on_submit():
        user = User(name=form.name.data, email=form.email.data,
                    password=form.password.data)
        db.session.add(user)
        db.session.commit()
        # f strings are allowed in pyhton 3.x
        flash(f'Account created for {form.name.data}', 'success')
        return redirect('/login')

    return render_template('signup.html', title='Messagez Signup', form=form)


@app.route('/newpost', methods=['POST', 'GET'])
def newpost():
  
  if 'email' not in session:
    flash('Login to Leave a Note', 'danger')
    return redirect('/login')
  
  form = MessageForm()
  owner = User.query.filter_by(email=session['email']).first()
  if form.validate_on_submit():
    message = Message(title=form.title.data, content=form.content.data, category=form.category.data, shift=form.shift.data, owner=owner)
    db.session.add(message)
    db.session.commit()
    flash("Posted Note Successfully", 'success')
    return redirect('/messages')

  return render_template('newpost.html', title='Message Post', form=form)


@app.route('/messages/', defaults={'category': ''})
@app.route('/messages/<category>')
def message(category):

  form = MessageForm()

  cat_lower = category.lower()
  if cat_lower == 'urgent':
      messages = Message.query.filter_by(
          category=cat_lower).filter_by(status=0).all()
      new_u = False
      if messages:
          new_u = True
      return render_template('messages.html', title="Urgent Messages", messages=messages, mark="Mark Completed", new_u=new_u, form=form)

  if cat_lower == 'general':
      messages = Message.query.filter_by(
          category=cat_lower).filter_by(status=0).all()
      new_g = False
      if messages:
          new_g = True
      return render_template('messages.html', title="General Messages", messages=messages, mark="Mark Completed", new_g=new_g, form=form)

  if cat_lower != 'urgent' and cat_lower != 'general':
      new_u = False
      new_g = False
      urgent_messages = Message.query.filter_by(
          category='urgent').filter_by(status=0).all()
      general_messages = Message.query.filter_by(
          category='general').filter_by(status=0).all()
      if urgent_messages:
          new_u = True
      if general_messages:
          new_g = True
      messages = Message.query.filter_by(status=0).all()
      return render_template('messages.html', title="Messages", messages=messages, mark="Mark Completed", new_g=new_g, new_u=new_u, form=form)


@app.route('/completed/', defaults={'id': ''})
@app.route('/completed/<int:id>', methods=['Get', 'POST'])
def mark_completion(id):
  form = MessageForm()
  completed_by = ''
  if request.method == 'POST':
    message = Message.query.filter_by(id=id).first()
    if 'email' not in session:
      flash('Login to Mark this Note', 'danger')
      return redirect('/login')
    if message.status == 1:
      message.status = 0
      db.session.commit()
      return redirect('/messages')
    else:
      message.status = 1
      db.session.commit()
      return redirect('/messages')
  user = user = User.query.filter_by(email=session['email']).first()
  completed_by = user.name
  messages = Message.query.filter_by(status=1).all()
  return render_template('messages.html', title="Completed Messages", messages=messages, mark="Unmark Completed", completed_by=completed_by, form=form)


@app.route('/messages/', defaults={'id': ''})
@app.route('/single/<int:id>', methods=['GET'])
def single(id):
  
  message = Message.query.filter_by(id=id).first()  
  
  form = MessageForm()  
  form.title.data = message.title
  form.category.data = message.category
  form.shift.data = message.shift
  form.content.data = message.content
  
  return render_template('single.html', message=message, form=form)


@app.route('/messages/', defaults={'id': ''})
@app.route('/single/<int:id>/delete', methods=['POST', 'GET'])
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


  return render_template('edit.html', title="Edit", form=form, message=message)


if __name__ == "__main__":
    app.run()
