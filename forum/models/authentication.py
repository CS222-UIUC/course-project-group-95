from flask import session
from . import models
from ..db import db


def create_user(username, password):
    new_user = models.User(username, password)

    db.session.add(new_user)
    db.session.commit()

    return new_user


def check_password(username, password):
    user = models.User.query.filter(username)
    if user == None:
        return "Username doesn't exist."
    # if user['password'] != password
    return user


def delete_all_user():
    print(models.User.query.delete())
    db.session.commit()
    return "All user deleted."


def list_all_user():
    users = models.User.query.all()
    return users


def get_current_user():
    return session.get('user_name')
