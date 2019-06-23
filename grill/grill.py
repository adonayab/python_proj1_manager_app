from flask import request, redirect, render_template, flash, Blueprint
from models import Food
from app import db

grill = Blueprint('grill', __name__)


@grill.route('/grill')
def index():
  foods = Food.query.all()
  return render_template('/grill/index.html', title='Virtual Grill', foods=foods)