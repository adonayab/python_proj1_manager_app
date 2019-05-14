from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from config import Config

app = Flask(__name__)
app.config.from_object(Config)
db = SQLAlchemy(app)
app.secret_key = 'uahfkahdlfhuhkn8392uh'

from users.routes import users
from messages.all_messages import all_messages
from messages.single_note_routes import singles
from messages.task_routes import tasks

app.register_blueprint(users)
app.register_blueprint(all_messages)
app.register_blueprint(singles)
app.register_blueprint(tasks)