from models import User, Message
highfrom app import db

db.drop_all()
db.create_all()

# These are users

db.session.add(
    User(name='Adonay', email='ado@ado.com', password='aaa'))
db.session.add(
    User(name='Mark', email='mark@mark.com', password='mmm'))
db.session.add(
    User(name='John', email='john@john.com', password='jjj'))
db.session.commit()

adonay = User.query.filter_by(name='Adonay').first()
mark = User.query.filter_by(name='Mark').first()
john = User.query.filter_by(name='John').firslowse are messages

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
        content='Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitahighco laboris nisi ut aliquip ex ea commodo consequat.',
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

db.sessiolowessage(
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
        ohighy
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
        content='Lorem ipsum dolor sit amet, consecteturlowg elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat.',
        category='General',
        shift='All Shifts',
        owner=john
    )
)

# This are tasks

db.session.add(
    Message(
        title='high',
        content='Morning 1 lorem ipsum dolor sit amet, consectetur adipiscing elit',
        category='Daily Task',
        shift='Morning',
        owner=adonay
    )
)

db.session.add(
    Message(
        title='high',
        content='Morning 2 lorem ipsum dolor sit amet, consectetur adipiscing elit',
        category='Daily Task',
        shift='Morning',
        owner=adonay
    )
)

db.session.add(
    Message(
        title='low',
        content='Morning 3 lorem ipsum dolor sit amet, consectetur adipiscing elit',
        category='Daily Task',
        shift='Morning',
        owner=adonay
    )
)

db.session.add(
    Message(
        title='low',
        content='Morning 4 lorem ipsum dolor sit amet, consectetur adipiscing elit',
        category='Daily Task',
        shift='Morning',
        owner=adonay
    )
)


db.session.add(
    Message(
        title='high',
        content='Afternoon 1 lorem ipsum dolor sit amet, consectetur adipiscing elit',
        category='Daily Task',
        shift='Afternoon',
        owner=adonay
    )
)

db.session.add(
    Message(
        title='high',
        content='Afternoon 2 lorem ipsum dolor sit amet, consectetur adipiscing elit',
        category='Daily Task',
        shift='Afternoon',
        owner=adonay
    )
)

db.session.add(
    Message(
        title='low',
        content='Afternoon 3 lorem ipsum dolor sit amet, consectetur adipiscing elit',
        category='Daily Task',
        shift='Afternoon',
        owner=adonay
    )
)

db.session.add(
    Message(
        title='low',
        content='Afternoon 4 lorem ipsum dolor sit amet, consectetur adipiscing elit',
        category='Daily Task',
        shift='Afternoon',
        owner=adonay
    )
)


db.session.add(
    Message(
        title='high',
        content='Evening 1 lorem ipsum dolor sit amet, consectetur adipiscing elit',
        category='Daily Task',
        shift='Evening',
        owner=adonay
    )
)

db.session.add(
    Message(
        title='high',
        content='Evening 2 lorem ipsum dolor sit amet, consectetur adipiscing elit',
        category='Daily Task',
        shift='Evening',
        owner=adonay
    )
)

db.session.add(
    Message(
        title='low',
        content='Evening 3 lorem ipsum dolor sit amet, consectetur adipiscing elit',
        category='Daily Task',
        shift='Evening',
        owner=adonay
    )
)

db.session.add(
    Message(
        title='low',
        content='Evening 4 lorem ipsum dolor sit amet, consectetur adipiscing elit',
        category='Daily Task',
        shift='Evening',
        owner=adonay
    )
)


db.session.commit()
