from sqlalchemy import Integer, DateTime, String, Column
from sqlalchemy.sql import func
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
