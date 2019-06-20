from flask import request, redirect, render_template, session, flash, Blueprint

grill = Blueprint('grill', __name__)


@grill.route('/grill')
def index():
  return render_template('/grill/index.html', title='Virtual Grill')