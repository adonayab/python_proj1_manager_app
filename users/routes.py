from flask import redirect, render_template, session, flash
from models import User
from app import db
from utils.hashutils import check_pw_hash
from users.forms import RegistrationForm, LoginForm


from flask import Blueprint

users = Blueprint('users', __name__)

# @users.before_request
# def require_login():
#     allowed_routes = ['login', 'signup', 'index', 'message']
#     if request.endpoint not in allowed_routes and 'email' not in session and '/static/' not in request.path:
#         return redirect('/login')


@users.route("/logout", methods=['POST'])
def logout():
    del session['email']
    return redirect('/login')


@users.route('/login', methods=['POST', 'GET'])
def login():
    if 'email' in session:
        return redirect('/messsages')
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


@users.route('/signup', methods=['POST', 'GET'])
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
