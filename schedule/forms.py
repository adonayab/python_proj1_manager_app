from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, TextAreaField, SelectField
from wtforms.validators import DataRequired

time_list = [('OFF', 'OFF'), (1, 1), (2, 2), (3, 3), (4, 4), (5, 5),
             (6, 6), (7, 7), (8, 8), (9, 9), (10, 10), (11, 11), (12, 12)]
time_state = [('OFF', 'OFF'), ('AM', 'AM'), ('PM', 'PM')]


class ScheduleForm(FlaskForm):
  
    start_friday = SelectField('', choices=time_list)
    start_friday_state = SelectField('', choices=time_state)
    end_friday = SelectField('', choices=time_list)
    end_friday_state = SelectField('', choices=time_state)

    start_saturday = SelectField('', choices=time_list)
    start_saturday_state = SelectField('', choices=time_state)
    end_saturday = SelectField('', choices=time_list)
    end_saturday_state = SelectField('', choices=time_state)

    start_sunday = SelectField('', choices=time_list)
    start_sunday_state = SelectField('', choices=time_state)
    end_sunday = SelectField('', choices=time_list)
    end_sunday_state = SelectField('', choices=time_state)

    start_monday = SelectField('', choices=time_list)
    start_monday_state = SelectField('', choices=time_state)
    end_monday = SelectField('', choices=time_list)
    end_monday_state = SelectField('', choices=time_state)

    start_tuesday = SelectField('', choices=time_list)
    start_tuesday_state = SelectField('', choices=time_state)
    end_tuesday = SelectField('', choices=time_list)
    end_tuesday_state = SelectField('', choices=time_state)

    start_wednesday = SelectField('', choices=time_list)
    start_wednesday_state = SelectField('', choices=time_state)
    end_wednesday = SelectField('', choices=time_list)
    end_wednesday_state = SelectField('', choices=time_state)

    start_thursday = SelectField('', choices=time_list)
    start_thursday_state = SelectField('', choices=time_state)
    end_thursday = SelectField('', choices=time_list)
    end_thursday_state = SelectField('', choices=time_state)
