from flask import redirect, render_template, session, flash, request
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
    return render_template('users/login.html', title='Login', form=form)


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

    return render_template('users/signup.html', title='Register', form=form)


@users.route('/admin', methods=['POST', 'GET'])
def admin():

    if 'email' not in session:
        flash('Log in as Admin', 'warning')
        return redirect('/login')

    current_user = User.query.filter_by(email=session['email']).first()
    if not current_user.admin:
        flash('Log in as Admin', 'warning')
        return redirect('/login')

    users = User.query.all()
    return render_template('users/admin.html', title='Admin', users=users)


@users.route('/admin/role', methods=['POST'])
def adminRoleChange():
    id = request.form['id']
    user = User.query.filter_by(id=id).first()
    if user.email == 'admin@admin.com':
        flash('Can not change ROLE of Master', 'warning')
        return redirect('/admin')
    if user.admin:
        user.admin = False
    else:
        user.admin = True

    db.session.add(user)
    db.session.commit()
    flash('Successfully changed ROLE', 'success')
    return redirect('/admin')


@users.route('/admin/delete', methods=['POST'])
def removeUser():
    id = request.form['id']
    user = User.query.filter_by(id=id).first()
    if user.email == 'admin@admin.com':
        flash('Can not delete Master', 'warning')
        return redirect('/admin')
    db.session.delete(user)
    db.session.commit()
    flash('Successfully deleted User', 'success')
    return redirect('/admin')
