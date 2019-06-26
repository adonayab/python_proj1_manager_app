from _datetime import datetime

from models import Message


def badge_urgent():
    urgent_messages = Message.query.filter_by(
        category='Urgent').filter_by(status=0).all()
    if urgent_messages:
        return True


def badge_general():
    general_messages = Message.query.filter_by(
        category='General').filter_by(status=0).all()
    if general_messages:
        return True


def message_query(category=None):
    if category == 'urgent':
        messages = Message.query.order_by(Message.pub_date.desc()).filter_by(
            category='Urgent').filter_by(status=0).paginate(per_page=5)
    elif category == 'general':
        messages = Message.query.order_by(Message.pub_date.desc()).filter_by(
            category='General').filter_by(status=0).paginate(per_page=5)
    elif category == 'completed':
        messages = Message.query.order_by(
            Message.pub_date.desc()).filter(
            Message.title != 'daily-task').filter_by(status=1).paginate(per_page=5)
    else:
        messages = Message.query.order_by(Message.pub_date.desc()).filter(
            Message.title != 'daily-task').filter_by(status=0).paginate(per_page=5)

    return messages


def day_format(str_day, full=True): # string = 2019-06-19 yy/mm/dd
    if not full:
        day = datetime.strptime(str_day, '%Y-%m-%d').strftime('%b %d, %Y')
        return day
    day = datetime.strptime(str_day, '%Y-%m-%d').strftime('%B %d, %Y')
    return day