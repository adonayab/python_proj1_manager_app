from flask import request, redirect, session, render_template, flash, Blueprint
from models import Food, User
from app import db

grill = Blueprint('grill', __name__)


@grill.route('/grill')
def index():
    foods = Food.query.all()
    return render_template('/grill/index.html', title='Virtual Grill', foods=foods)


@grill.route('/grill/addFood', methods=['POST'])
def addFood():

    if 'email' not in session:
        flash('Login as Admin to Add Food Item', 'danger')
        return redirect('/grill')

    owner = User.query.filter_by(email=session['email']).first()
    if not owner.admin:
        flash("Login as Admin to  Add Food Item", 'danger')
        return redirect('/grill')

    foods = Food.query.all()

    if 'name' in request.form:
        name = request.form['name']
        cook_time = request.form['cook-time']
        for food in foods:
            if name == food.name:
                flash("Duplicate Food Item", 'danger')
                return redirect('/grill')

        food = Food(name=name, cook_time=cook_time)
        db.session.add(food)
        db.session.commit()
        flash("Food Item was added successfully", 'success')
        return redirect('/grill')

    return redirect('/grill')


@grill.route('/grill/delete', methods=['POST'])
def deleteFood():
    if 'email' not in session:
        flash('Login as Admin to Delete Food Item', 'danger')
        return redirect('/grill')

    owner = User.query.filter_by(email=session['email']).first()
    if not owner.admin:
        flash("Login as Admin to  Delete Food Item", 'danger')
        return redirect('/grill')

    if 'id' in request.form:
        id = request.form['id']
        food = Food.query.filter_by(id=id).first()
        db.session.delete(food)
        db.session.commit()
        flash("Food Item was Deleted successfully", 'success')
        return redirect('/grill')

    return '/grill'
