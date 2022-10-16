from ..db import db


# Declaring database tables


# Declare user table, with username as primary key, and password, both is sql string.
class User(db.Model):

    username = db.Column(db.String, primary_key=True)
    password = db.Column(db.String)

    def __init__(self, username, password):
        self.username = username
        self.password = password
