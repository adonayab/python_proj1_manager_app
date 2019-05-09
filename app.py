from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from config import Config

app = Flask(__name__)
app.config.from_object(Config)
db = SQLAlchemy(app)
app.secret_key = 'uahfkahdlfhuhkn8392uh'

from users.routes import users
from notes.note_routes import notes
from notes.task_routes import tasks

app.register_blueprint(users)
app.register_blueprint(notes)
app.register_blueprint(tasks)