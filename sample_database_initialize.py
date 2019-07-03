from app import db
from models import User, Message, WeekSchedule, UserSchedule, Food, DaysOfSchedule
import random

db.drop_all()
db.create_all()

# These are users
admin = User(name='Admin', email='admin@admin.com', password='admin')
adonay = User(name='Adonay', email='ado@ado.com', password='aaa')
mark = User(name='Mark', email='mark@mark.com', password='mmm')
john = User(name='John', email='john@john.com', password='jjj')
gary = User(name='Gary', email='gary@gary.com', password='ggg')
bev = User(name='Bev', email='bev@bev.com', password='bbb')
tracy = User(name='Tracy', email='tracy@tracy.com', password='ttt')

admin.admin = True

db.session.add(adonay)
db.session.add(mark)
db.session.add(john)
db.session.add(admin)

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
        title='Mark Urgent',
        content='Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat.',
        category='Urgent',
        shift='All Shifts',
        owner=mark
    )
)
db.session.add(
    Message(
        title='Mark General',
        content='Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat.',
        category='General',
        shift='All Shifts',
        owner=mark
    )
)


db.session.add(
    Message(
        title='Mark to Morning',
        content='Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat.',
        category='Urgent',
        shift='Morning',
        owner=mark
    )
)
db.session.add(
    Message(
        title='Mark to Evening',
        content='Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat.',
        category='Urgent',
        shift='Afternoon',
        owner=mark
    )
)
db.session.add(
    Message(
        title='Mark to Afternoon',
        content='Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat.',
        category='General',
        shift='Evening',
        owner=mark
    )
)


db.session.add(
    Message(
        title='By John',
        content='Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat.',
        category='Urgent',
        shift='All Shifts',
        owner=john
    )
)
db.session.add(
    Message(
        title='John Urgent',
        content='Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat.',
        category='Urgent',
        shift='All Shifts',
        owner=john
    )
)
db.session.add(
    Message(
        title='John General',
        content='Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat.',
        category='General',
        shift='All Shifts',
        owner=john
    )
)

db.session.add(
    Message(
        title='John to Morning',
        content='Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat.',
        category='Urgent',
        shift='Morning',
        owner=john
    )
)
db.session.add(
    Message(
        title='John to Evening',
        content='Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat.',
        category='General',
        shift='Afternoon',
        owner=john
    )
)
db.session.add(
    Message(
        title='John to Afternoon',
        content='Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat.',
        category='General',
        shift='Evening',
        owner=john
    )
)

db.session.add(
    Message(
        title='By Tracy',
        content='Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat.',
        category='General',
        shift='All Shifts',
        owner=tracy
    )
)
db.session.add(
    Message(
        title='Tracy Urgent',
        content='Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat.',
        category='Urgent',
        shift='All Shifts',
        owner=tracy
    )
)
db.session.add(
    Message(
        title='Tracy General',
        content='Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat.',
        category='General',
        shift='All Shifts',
        owner=tracy
    )
)


db.session.add(
    Message(
        title='Tracy to Morning',
        content='Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat.',
        category='Urgent',
        shift='Morning',
        owner=tracy
    )
)
db.session.add(
    Message(
        title='Tracy to Evening',
        content='Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat.',
        category='Urgent',
        shift='Afternoon',
        owner=tracy
    )
)
db.session.add(
    Message(
        title='Tracy to Afternoon',
        content='Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat.',
        category='General',
        shift='Evening',
        owner=tracy
    )
)


db.session.add(
    Message(
        title='By Bev',
        content='Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat.',
        category='Urgent',
        shift='All Shifts',
        owner=bev
    )
)
db.session.add(
    Message(
        title='Bev Urgent',
        content='Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat.',
        category='Urgent',
        shift='All Shifts',
        owner=bev
    )
)
db.session.add(
    Message(
        title='Bev General',
        content='Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat.',
        category='General',
        shift='All Shifts',
        owner=bev
    )
)

db.session.add(
    Message(
        title='Bev to Morning',
        content='Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat.',
        category='Urgent',
        shift='Morning',
        owner=bev
    )
)
db.session.add(
    Message(
        title='Bev to Evening',
        content='Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat.',
        category='General',
        shift='Afternoon',
        owner=bev
    )
)
db.session.add(
    Message(
        title='Bev to Afternoon',
        content='Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat.',
        category='General',
        shift='Evening',
        owner=bev
    )
)


#################
# This are tasks
#################

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

######################
# Generating schedules
######################

from utils.helpers import get_date, days_generator

w_1_s = get_date('2019-07-02')
w_2_s = get_date('2019-07-05')
w_3_s = get_date('2019-08-07')
w_4_s = get_date('2019-08-05')

w_1_e = get_date('2019-07-08')
w_2_e = get_date('2019-07-11')
w_3_e = get_date('2019-08-13')
w_4_e = get_date('2019-08-11')

w_1 = WeekSchedule(start_date=w_1_s, end_date=w_1_e)
w_2 = WeekSchedule(start_date=w_2_s, end_date=w_2_e)
w_3 = WeekSchedule(start_date=w_3_s, end_date=w_3_e)
w_4 = WeekSchedule(start_date=w_4_s, end_date=w_4_e)

db.session.add(w_1)
db.session.add(w_2)
db.session.add(w_3)
db.session.add(w_4)

db.session.commit()

start_day_1 = w_1.start_date.strftime("%A")
start_day_2 = w_2.start_date.strftime("%A")
start_day_3 = w_3.start_date.strftime("%A")
start_day_4 = w_4.start_date.strftime("%A")

days_of_week_1 = days_generator(start_day_1)
days_of_week_2 = days_generator(start_day_2)
days_of_week_3 = days_generator(start_day_3)
days_of_week_4 = days_generator(start_day_4)

us1_w_1 = UserSchedule(name=john.name, week=w_1)
us2_w_1 = UserSchedule(name=adonay.name, week=w_1)
us3_w_1 = UserSchedule(name=mark.name, week=w_1)
us4_w_1 = UserSchedule(name=gary.name, week=w_1)
us5_w_1 = UserSchedule(name=bev.name, week=w_1)
us6_w_1 = UserSchedule(name=tracy.name, week=w_1)

usrs = [us1_w_1, us2_w_1, us3_w_1, us4_w_1, us5_w_1, us6_w_1]

for usr in usrs:
    tims = ['7 AM', 'OFF', '8 AM', '9 AM', '1 AM', '2 AM', '10 AM', '11 AM', '6 AM', '3 AM', '12 AM', 'OFF']
    for day in days_of_week_1:
        tim_in = random.choice(tims)
        tim_out = random.choice(tims)
        if tim_in == tim_out:
            tim_out = random.choice(tims)
        if 'OFF' == tim_in or tim_out == 'OFF':
            tim_in = 'OFF'
            tim_out = 'OFF'
        db.session.add(DaysOfSchedule(day=day, usr_sch=usr, tim_in=tim_in, tim_out=tim_out))


us1_w_2 = UserSchedule(name=adonay.name, week=w_2)
us2_w_2 = UserSchedule(name=john.name, week=w_2)
us3_w_2 = UserSchedule(name=mark.name, week=w_2)
us4_w_2 = UserSchedule(name=bev.name, week=w_2)
us5_w_2 = UserSchedule(name=tracy.name, week=w_2)
us6_w_2 = UserSchedule(name=gary.name, week=w_2)

usrs = [us1_w_2, us2_w_2, us3_w_2, us4_w_2, us5_w_2, us6_w_2]

for usr in usrs:
    tims = ['7 AM', 'OFF', '8 AM', '9 AM', '1 AM', '2 AM', '10 AM', '11 AM', '6 AM', '3 AM', '12 AM', 'OFF']
    for day in days_of_week_2:
        tim_in = random.choice(tims)
        tim_out = random.choice(tims)
        if tim_in == tim_out:
            tim_out = random.choice(tims)
        if 'OFF' == tim_in or tim_out == 'OFF':
            tim_in = 'OFF'
            tim_out = 'OFF'
        db.session.add(DaysOfSchedule(day=day, usr_sch=usr, tim_in=tim_in, tim_out=tim_out))


us1_w_3 = UserSchedule(name=gary.name, week=w_3)
us2_w_3 = UserSchedule(name=john.name, week=w_3)
us3_w_3 = UserSchedule(name=bev.name, week=w_3)
us4_w_3 = UserSchedule(name=tracy.name, week=w_3)
us5_w_3 = UserSchedule(name=mark.name, week=w_3)
us6_w_3 = UserSchedule(name=adonay.name, week=w_3)

usrs = [us1_w_3, us2_w_3, us3_w_3, us4_w_3, us5_w_3, us6_w_3]

for usr in usrs:
    tims = ['7 AM', 'OFF', '8 AM', '9 AM', '1 AM', '2 AM', '10 AM', '11 AM', '6 AM', '3 AM', '12 AM', 'OFF']
    for day in days_of_week_3:
        tim_in = random.choice(tims)
        tim_out = random.choice(tims)
        if tim_in == tim_out:
            tim_out = random.choice(tims)
        if 'OFF' == tim_in or tim_out == 'OFF':
            tim_in = 'OFF'
            tim_out = 'OFF'
        db.session.add(DaysOfSchedule(day=day, usr_sch=usr, tim_in=tim_in, tim_out=tim_out))


us1_w_4 = UserSchedule(name=john.name, week=w_4)
us2_w_4 = UserSchedule(name=gary.name, week=w_4)
us3_w_4 = UserSchedule(name=mark.name, week=w_4)
us4_w_4 = UserSchedule(name=tracy.name, week=w_4)
us5_w_4 = UserSchedule(name=adonay.name, week=w_4)
us6_w_4 = UserSchedule(name=bev.name, week=w_4)

usrs = [us1_w_4, us2_w_4, us3_w_4, us4_w_4, us5_w_4, us6_w_4]

for usr in usrs:
    tims = ['7 AM', 'OFF', '8 AM', '9 AM', '1 AM', '2 AM', '10 AM', '11 AM', '6 AM', '3 AM', '12 AM', 'OFF']
    for day in days_of_week_4:
        tim_in = random.choice(tims)
        tim_out = random.choice(tims)
        if tim_in == tim_out:
            tim_out = random.choice(tims)
        if 'OFF' == tim_in or tim_out == 'OFF':
            tim_in = 'OFF'
            tim_out = 'OFF'
        db.session.add(DaysOfSchedule(day=day, usr_sch=usr, tim_in=tim_in, tim_out=tim_out))


db.session.add(us1_w_1)
db.session.add(us2_w_1)
db.session.add(us3_w_1)

db.session.add(us1_w_2)
db.session.add(us2_w_2)
db.session.add(us3_w_2)

db.session.add(us1_w_3)
db.session.add(us2_w_3)
db.session.add(us3_w_3)

db.session.add(us1_w_4)
db.session.add(us2_w_4)
db.session.add(us3_w_4)


########
# Foods
########

f1 = Food(name="Hot Dog", cook_time=30)
f2 = Food(name="BBQ Hot Dog", cook_time=30)
f3 = Food(name="Chs Brg Bite", cook_time=30)
f4 = Food(name="Taco Chs", cook_time=20)
f5 = Food(name="Mont Jack", cook_time=20)
f6 = Food(name="Chk Rnch", cook_time=20)

db.session.add(f1)
db.session.add(f2)
db.session.add(f3)
db.session.add(f4)
db.session.add(f5)
db.session.add(f6)

db.session.commit()
