from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField, TextAreaField,SelectField
from wtforms.validators import DataRequired, Length, Email, EqualTo, ValidationError
from models import User


class RegistrationForm(FlaskForm):
    name = StringField('Name', validators=[
        DataRequired(), Length(min=3, max=20)])
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    confirm_password = PasswordField('Confirm Password', validators=[
                                     DataRequired(), EqualTo('password')])
    submit = SubmitField('Sign Up')

    def validate_name(self, name):
        user = User.query.filter_by(name=name.data).first()
        if user:
            raise ValidationError('A user with the same name exists.')

    def validate_email(self, email):
        user = User.query.filter_by(email=email.data).first()
        if user:
            raise ValidationError('A user with the same email exists.')


class LoginForm(FlaskForm):
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    submit = SubmitField('Login')

class MessageForm(FlaskForm):
  title = StringField('Title', validators=[DataRequired()])
  content = TextAreaField('Content', validators=[DataRequired()])
  category = SelectField(
        'Category',
        choices=[('Urgent','Urgent'), ('General','General'), ('Daily Task','Daily Task')]
    )
  shift = SelectField(
        'Shift',
        choices=[('All Shifts','All Shifts'), ('Morning','Morning'), ('Afternoon','Afternoon'),  ('Evening','Evening')]
    )
  submit = SubmitField('Post Note')
  

class TaskForm(FlaskForm):
  content = TextAreaField('Content', validators=[DataRequired()])
  shift = SelectField(
        'Shift',
        choices=[('All Shifts','All Shifts'), ('Morning','Morning'), ('Afternoon','Afternoon'),  ('Evening','Evening')]
    )
  submit = SubmitField('Add Task')
  