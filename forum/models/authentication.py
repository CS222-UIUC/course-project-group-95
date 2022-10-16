from flask import session
from . import models
from ..db import db


# Create new user in the database, SQL Integrity Error is catched in views.py
def create_user(username, password):
    new_user = models.User(username, password)

    db.session.add(new_user)
    db.session.commit()

    return new_user


# Check password for the input username and password, return username if there is a match
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


# Delete all elements in the User table
def delete_all_user():
    print(models.User.query.delete())
    db.session.commit()
    return "All user deleted."


# Returns all the users stored in User
def list_all_user():
    users = models.User.query.all()
    return users
