from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from config import Config

app = Flask(__name__)
app.config.from_object(Config)
db = SQLAlchemy(app)
app.secret_key = 'uahfkahdlfhuhkn8392uh'

from users.routes import users
from messages.all_messages import all_messages
from messages.single_messages import single_messages
from messages.tasks import tasks
from schedule.schedule import schedules
from grill.grill import grill

app.register_blueprint(users)
app.register_blueprint(all_messages)
app.register_blueprint(single_messages)
app.register_blueprint(tasks)
app.register_blueprint(schedules)
app.register_blueprint(grill)