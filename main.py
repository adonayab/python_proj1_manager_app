from flask import Flask, request, redirect, render_template, session, flash
from flask_sqlalchemy import SQLAlchemy
from models import User, Message
from app import app, db
import re
from hashutils import check_pw_hash
from datetime import datetime


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
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']
        user = User.query.filter_by(email=email).first()
        if user and check_pw_hash(password, user.pw_hash):
            session['email'] = email
            flash("Logged in")
            return redirect('/Message')
        elif user and user.pw_hash != password:
            flash('Incorrect password')
        elif email == '' and password == '':
            flash('Email and Password required')
        else:
            flash('User does not exist')

    return render_template('login.html', title='Messagez Login')


@app.route('/signup', methods=['POST', 'GET'])
def signup():

    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']
        verify = request.form['verify']
        name = request.form['name']

        if verify == password:
            user = User(name=name, email=email, password=password)
            db.session.add(user)
            db.session.commit()
            session['email'] = email
            return redirect('/')
        else:
            return redirect('/signup')

    return render_template('signup.html', title='Messagez Signup')


@app.route('/newpost', methods=['POST', 'GET'])
def newpost():

    if request.method == 'POST':
        title = request.form['title']
        body = request.form['body']
        category = request.form['category']
        owner = User.query.filter_by(email='ado@ado.com').first()

        if title == '' or body == '':
            flash("The title or body can not be empty.")
            return redirect('/newpost')

        new_Message = Message(title, body, category, owner)
        db.session.add(new_Message)
        db.session.commit()
        return redirect('/')

    return render_template('newpost.html', title='Messagez Post')

@app.route('/')
@app.route('/message', methods=['POST', 'GET'])
def message():

    messages = Message.query.all()

    return render_template('message.html', title="Messages", messages=messages)


if __name__ == "__main__":
    app.run()
