from sqlalchemy import Integer, DateTime, String, Column
from ..db import db


# Declaring database tables


# Declare user table, with username as primary key, and password, both is sql string.
class User(db.Model):
    username = Column(String, primary_key=True)
    password = Column(String)

    def __init__(self, username, password):
        self.username = username
        self.password = password


# Declare post table, with post_id (auto_increment) as primary key;
#       title, author, and content as sql string; and creation time as sql DateTime.
class Post(db.Model):
    id = Column(Integer, primary_key=True)
    title = Column(String)
    author = Column(String)
    content = Column(String)
    create_datetime = Column(DateTime)

    def __init__(self, title, author, create_datetime,  content):
        self.title = title
        self.author = author
        self.content = content
        self.create_datetime = create_datetime


# Declare message table, with id (auto_increment) as primary key;
#       sender, receiver, and content as sql string; and sent_datetime as sql DateTime.
class Message(db.Model):
    id = Column(Integer, primary_key=True)
    sender = Column(String)
    receiver = Column(String)
    content = Column(String)
    sent_datetime = Column(DateTime)

    def __init__(self, sender, receiver, content, sent_datetime):
        self.sender = sender
        self.receiver = receiver
        self.content = content
        self.sent_datetime = sent_datetime


# Declare connection table, with id (auto_increment) as primary key;
#       sender and receiver as sql string; and last_contact_datetime as sql DateTime.
# For existing connection, status is 0
# For pending connection, status is 1, contact time is sent time
class Connection(db.Model):
    id = Column(Integer, primary_key=True)
    sender = Column(String)
    receiver = Column(String)
    status = Column(Integer)
    last_contact_datetime = Column(DateTime)

    def __init__(self, sender, receiver, status, last_contact_datetime):
        self.sender = sender
        self.receiver = receiver
        self.status = status
        self.last_contact_datetime = last_contact_datetime
