from . import models
from ..db import db
from datetime import datetime
import pytz


# Return all the connections of user
def get_connections(user):
    connection_as_sender = models.Connection.query.filter_by(sender=user, status=0).with_entities(
        models.Connection.receiver.label('username'), models.Connection.last_contact_datetime)

    connection_as_receiver = models.Connection.query.filter_by(receiver=user, status=0).with_entities(
        models.Connection.sender.label('username'), models.Connection.last_contact_datetime)

    return connection_as_sender.union(connection_as_receiver).order_by(
        models.Connection.last_contact_datetime.desc()).with_entities(db.column('username')).all()


# Return all the message history between user1 and user2
def get_message_history(user1, user2):
    return models.Message.query.filter_by(sender=user1, receiver=user2).union(
        models.Message.query.filter_by(sender=user2, receiver=user1)).order_by(
        models.Message.sent_datetime).all()


# Insert into database of the sent message
# Also update the last_contact_datetime of the connection between sender and receiver
def send_message(sender, receiver, content):
    tz = pytz.timezone('US/Central')
    cur_time = datetime.now(tz=tz)
    new_message = models.Message(sender, receiver, content, cur_time)

    db.session.add(new_message)
    db.session.commit()

    models.Connection.query.filter_by(sender=sender, receiver=receiver).update(
        {'last_contact_datetime': cur_time})
    models.Connection.query.filter_by(receiver=sender, sender=receiver).update(
        {'last_contact_datetime': cur_time})
    db.session.commit()

    return new_message


# Delete all private message
# For testing
def delete_all_pm():
    models.Message.query.delete()
    db.session.commit()


# Search user by username
def search_user(keyword):
    return models.User.query.filter_by(username=keyword).all()


# Insert into database the connection request from sender to receiver
def send_connection_request(sender, receiver):
    tz = pytz.timezone('US/Central')
    cur_time = datetime.now(tz=tz)
    connection_request = models.Connection(sender, receiver, 1, cur_time)

    db.session.add(connection_request)
    db.session.commit()

    return connection_request


# Update the connection request to connection between sender and receiver
def add_connection(sender, receiver):
    tz = pytz.timezone('US/Central')
    cur_time = datetime.now(tz=tz)
    models.Connection.query.filter_by(sender=sender, receiver=receiver).update(
        {'last_contact_datetime': cur_time, 'status': 0}
    )
    db.session.commit()


# Delete the connection request from sender to receiver
def delete_connection_request(sender, receiver):
    models.Connection.query.filter_by(
        sender=sender, receiver=receiver, status=1).delete()
    db.session.commit()


# Delete the connection between sender and receiver
def delete_connection(sender, receiver):
    models.Connection.query.filter_by(
        sender=sender, receiver=receiver, status=0).delete()
    models.Connection.query.filter_by(
        sender=receiver, receiver=sender, status=0).delete()
    db.session.commit()


# Return true if there is already a connection request from sender to receiver
def check_request_exist(sender, receiver):
    check = models.Connection.query.filter_by(sender=sender, receiver=receiver, status=1).union(
        models.Connection.query.filter_by(sender=receiver, receiver=sender, status=1)).all()
    return len(check) != 0


# Return all pending connection requests sent by the current user
def get_pending_sent_request(user):
    return models.Connection.query.filter_by(sender=user, status=1).order_by(
        models.Connection.last_contact_datetime.desc()).all()


# Return all the pending connections waiting for current user's approval
def get_pending_received_request(user):
    return models.Connection.query.filter_by(receiver=user, status=1).order_by(
        models.Connection.last_contact_datetime.desc()).all()
