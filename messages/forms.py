from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, TextAreaField, SelectField, RadioField
from wtforms.validators import DataRequired


class MessageForm(FlaskForm):
    title = StringField('Title', validators=[DataRequired()])
    content = TextAreaField('Content', validators=[DataRequired()])
    category = SelectField(
        'Category',
        choices=[('Urgent', 'Urgent'), ('General', 'General')]
    )
    shift = SelectField(
        'Shift',
        choices=[('All Shifts', 'All Shifts'), ('Morning', 'Morning'),
                 ('Afternoon', 'Afternoon'),  ('Evening', 'Evening')]
    )
    submit = SubmitField('Post Note')


class TaskForm(FlaskForm):
    content = TextAreaField('Content', validators=[DataRequired()])
    category = RadioField('Priority', choices=[
                          ('high', 'High'), ('low', 'Low')], default='high')
    shift = SelectField(
        'Shift',
        choices=[('Morning', 'Morning'), ('Afternoon',
                                          'Afternoon'),  ('Evening', 'Evening')]
    )
    submit = SubmitField('Add Task')
