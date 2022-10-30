from . import models
from ..db import db
from datetime import datetime
import pytz


# Return all the connections of user
def get_connections(user):
    connection_as_first = models.Connection.query.filter_by(first=user).with_entities(
        models.Connection.second.label('username'), models.Connection.last_contact_datetime)

    connection_as_second = models.Connection.query.filter_by(second=user).with_entities(
        models.Connection.first.label('username'), models.Connection.last_contact_datetime)

    return connection_as_first.union(connection_as_second).order_by(
        models.Connection.last_contact_datetime.desc()).with_entities(db.column('username')).all()


# Add connection between user1 and user2
def add_connection(user1, user2):
    tz = pytz.timezone('US/Central')
    cur_time = datetime.now(tz=tz)
    new_connection = models.Connection(user1, user2, cur_time)

    db.session.add(new_connection)
    db.session.commit()

    return new_connection


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

    models.Connection.query.filter_by(first=sender, second=receiver).update(
        {'last_contact_datetime': cur_time})
    models.Connection.query.filter_by(second=sender, first=receiver).update(
        {'last_contact_datetime': cur_time})
    db.session.commit()

    return new_message
