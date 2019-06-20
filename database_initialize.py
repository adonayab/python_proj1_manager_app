from app import db
from models import User, Message, WeekSchedule, UserSchedule

db.drop_all()
db.create_all()

# These are users

adonay = User(name='Adonay', email='ado@ado.com', password='aaa')
mark = User(name='Mark', email='mark@mark.com', password='mmm')
john = User(name='John', email='john@john.com', password='jjj')

db.session.add(adonay)
db.session.add(mark)
db.session.add(john)

db.session.commit()

# These are messages

db.session.add(
    Message(
        title='Urgent',
        content='Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat.',
        category='Urgent',
        shift='All Shifts',
        owner=adonay
    )
)

db.session.add(
    Message(
        title='General',
        content='Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat.',
        category='General',
        shift='All Shifts',
        owner=adonay
    )
)

db.session.add(
    Message(
        title='Completed',
        content='Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat.',
        category='Urgent',
        shift='Afternoon',
        owner=adonay
    )
)

db.session.add(
    Message(
        title='To be Edited',
        content='Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat.',
        category='General',
        shift='Evening',
        owner=adonay
    )
)

db.session.add(
    Message(
        title='To be Deleted',
        content='Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat.',
        category='Urgent',
        shift='Morning',
        owner=adonay
    )
)

db.session.add(
    Message(
        title='By Mark',
        content='Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat.',
        category='General',
        shift='All Shifts',
        owner=mark
    )
)

db.session.add(
    Message(
        title='By John',
        content='Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat.',
        category='General',
        shift='All Shifts',
        owner=john
    )
)

# This are tasks

db.session.add(
    Message(
        title='daily-task',
        content='Morning 1 lorem ipsum dolor sit amet, consectetur adipiscing elit',
        category='low',
        shift='Morning',
        owner=adonay
    )
)

db.session.add(
    Message(
        title='daily-task',
        content='Morning 2 lorem ipsum dolor sit amet, consectetur adipiscing elit',
        category='low',
        shift='Morning',
        owner=adonay
    )
)

db.session.add(
    Message(
        title='daily-task',
        content='Morning 3 lorem ipsum dolor sit amet, consectetur adipiscing elit',
        category='high',
        shift='Morning',
        owner=adonay
    )
)

db.session.add(
    Message(
        title='daily-task',
        content='Morning 4 lorem ipsum dolor sit amet, consectetur adipiscing elit',
        category='high',
        shift='Morning',
        owner=adonay
    )
)


db.session.add(
    Message(
        title='daily-task',
        content='Afternoon 1 lorem ipsum dolor sit amet, consectetur adipiscing elit',
        category='low',
        shift='Afternoon',
        owner=adonay
    )
)

db.session.add(
    Message(
        title='daily-task',
        content='Afternoon 2 lorem ipsum dolor sit amet, consectetur adipiscing elit',
        category='low',
        shift='Afternoon',
        owner=adonay
    )
)

db.session.add(
    Message(
        title='daily-task',
        content='Afternoon 3 lorem ipsum dolor sit amet, consectetur adipiscing elit',
        category='high',
        shift='Afternoon',
        owner=adonay
    )
)

db.session.add(
    Message(
        title='daily-task',
        content='Afternoon 4 lorem ipsum dolor sit amet, consectetur adipiscing elit',
        category='high',
        shift='Afternoon',
        owner=adonay
    )
)


db.session.add(
    Message(
        title='daily-task',
        content='Evening 1 lorem ipsum dolor sit amet, consectetur adipiscing elit',
        category='low',
        shift='Evening',
        owner=adonay
    )
)

db.session.add(
    Message(
        title='daily-task',
        content='Evening 2 lorem ipsum dolor sit amet, consectetur adipiscing elit',
        category='low',
        shift='Evening',
        owner=adonay
    )
)

db.session.add(
    Message(
        title='daily-task',
        content='Evening 3 lorem ipsum dolor sit amet, consectetur adipiscing elit',
        category='high',
        shift='Evening',
        owner=adonay
    )
)

db.session.add(
    Message(
        title='daily-task',
        content='Evening 4 lorem ipsum dolor sit amet, consectetur adipiscing elit',
        category='high',
        shift='Evening',
        owner=adonay
    )
)


# Generating schedules

week1 = '2019/05/03 to 2019/05/09'
week2 = '2019/05/31 to 2019/06/07'
week3 = '2019/06/07 to 2019/06/13'
week4 = '2019/05/13 to 2019/05/19'

ws1 = WeekSchedule(on_week=week1)
ws2 = WeekSchedule(on_week=week2)
ws3 = WeekSchedule(on_week=week3)
ws4 = WeekSchedule(on_week=week4)

db.session.add(ws1)
db.session.add(ws2)
db.session.add(ws3)
db.session.add(ws4)

db.session.commit()

us1_w1 = UserSchedule(name=adonay.name, week=ws1)
us2_w1 = UserSchedule(name=mark.name, week=ws1)
us3_w1 = UserSchedule(name=john.name, week=ws1)

us1_w1.monday = '7AM - 2PM'
us1_w1.tuesday = 'OFF'
us1_w1.wednesday = '7AM - 2PM'
us1_w1.thursday = 'OFF'
us1_w1.friday = '7AM - 2PM'
us1_w1.saturday = '10AM - 7AM'
us1_w1.sunday = '7AM - 2PM'

us2_w1.monday = '2PM - 10PM'
us2_w1.tuesday = '7AM - 2PM'
us2_w1.wednesday = '2PM - 10PM'
us2_w1.thursday = 'OFF'
us2_w1.friday = '2PM - 10PM'
us2_w1.saturday = 'OFF'
us2_w1.sunday = '2PM - 10PM'

us3_w1.monday = '10AM - 7AM'
us3_w1.tuesday = 'OFF'
us3_w1.wednesday = '10AM - 7AM'
us3_w1.thursday = '7AM - 2PM'
us3_w1.friday = '10AM - 7AM'
us3_w1.saturday = 'OFF'
us3_w1.sunday = '10AM - 7AM'


us1_w2 = UserSchedule(name=john.name, week=ws2)
us2_w2 = UserSchedule(name=adonay.name, week=ws2)
us3_w2 = UserSchedule(name=mark.name, week=ws2)

us1_w2.monday = '7AM - 2PM'
us1_w2.tuesday = 'OFF'
us1_w2.wednesday = '7AM - 2PM'
us1_w2.thursday = 'OFF'
us1_w2.friday = '7AM - 2PM'
us1_w2.saturday = '10AM - 7AM'
us1_w2.sunday = '7AM - 2PM'

us2_w2.monday = '2PM - 10PM'
us2_w2.tuesday = '7AM - 2PM'
us2_w2.wednesday = '2PM - 10PM'
us2_w2.thursday = 'OFF'
us2_w2.friday = '2PM - 10PM'
us2_w2.saturday = 'OFF'
us2_w2.sunday = '2PM - 10PM'

us3_w2.monday = '10AM - 7AM'
us3_w2.tuesday = 'OFF'
us3_w2.wednesday = '10AM - 7AM'
us3_w2.thursday = '7AM - 2PM'
us3_w2.friday = '10AM - 7AM'
us3_w2.saturday = 'OFF'
us3_w2.sunday = '10AM - 7AM'

us1_w3 = UserSchedule(name=mark.name, week=ws3)
us2_w3 = UserSchedule(name=john.name, week=ws3)
us3_w3 = UserSchedule(name=adonay.name, week=ws3)

us1_w3.monday = '7AM - 2PM'
us1_w3.tuesday = 'OFF'
us1_w3.wednesday = '7AM - 2PM'
us1_w3.thursday = 'OFF'
us1_w3.friday = '7AM - 2PM'
us1_w3.saturday = '10AM - 7AM'
us1_w3.sunday = '7AM - 2PM'

us2_w3.monday = '2PM - 10PM'
us2_w3.tuesday = '7AM - 2PM'
us2_w3.wednesday = '2PM - 10PM'
us2_w3.thursday = 'OFF'
us2_w3.friday = '2PM - 10PM'
us2_w3.saturday = 'OFF'
us2_w3.sunday = '2PM - 10PM'

us3_w3.monday = '10AM - 7AM'
us3_w3.tuesday = 'OFF'
us3_w3.wednesday = '10AM - 7AM'
us3_w3.thursday = '7AM - 2PM'
us3_w3.friday = '10AM - 7AM'
us3_w3.saturday = 'OFF'
us3_w3.sunday = '10AM - 7AM'

db.session.add(us1_w1)
db.session.add(us2_w1)
db.session.add(us3_w1)

db.session.add(us1_w2)
db.session.add(us2_w2)
db.session.add(us3_w2)

db.session.add(us1_w3)
db.session.add(us2_w3)
db.session.add(us3_w3)

db.session.commit()
