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
            category='Urgent').filter_by(status=0).all()
    elif category == 'general':
        messages = Message.query.order_by(Message.pub_date.desc()).filter_by(
            category='General').filter_by(status=0).all()
    else:
        messages = Message.query.order_by(Message.pub_date.desc()).filter(
            Message.title != 'daily-task').filter_by(status=0).all()

    return messages
