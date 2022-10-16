from flask import session
from . import models
from ..db import db


def create_user(username, password):
    new_user = models.User(username, password)

    db.session.add(new_user)
    db.session.commit()

    return new_user


def check_password(username, password):
    try:
        user_with_correct_name = models.User.query.filter_by(
            username=username).one()
    except:
        return "Username doesn't exist."
    try:
        user_with_correct_password = models.User.query.filter_by(
            username=username, password=password).one()
    except:
        return "Password incorrect."

    print(user_with_correct_password.username)

    return user_with_correct_password


def delete_all_user():
    print(models.User.query.delete())
    db.session.commit()
    return "All user deleted."


def list_all_user():
    users = models.User.query.all()
    return users


def get_current_user():
    return session.get('user_name')
