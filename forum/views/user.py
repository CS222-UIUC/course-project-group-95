from flask import flash, redirect, render_template, request, Blueprint, url_for, session
from ..models import authentication, post
from sqlalchemy import exc


# Register blueprint for user operations
blueprint = Blueprint('user', __name__, url_prefix='/user/')


# Register page:
# Flash warning messages when username or password is not given or when username already exists
# Redirect to login page if registered successfully
@blueprint.route('/register', methods=('GET', 'POST'))
def register():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        message = None

        if not username:
            message = 'Username is required.'
        elif not password:
            message = 'Password is required.'
        else:
            try:
                authentication.create_user(username, password)
                return redirect(url_for('user.login'))
            except exc.IntegrityError:
                message = 'Username exists.'

        flash(message)

    return render_template('auth/register.html')


# Login page:
# Flash warning messages when username or password is not given
#                       or when username and password doesn't match
# Redirect to index page and register user in session if logged in successfully
@blueprint.route('/login', methods=('GET', 'POST'))
def login():

    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        message = None

        if not username:
            message = 'Username is required.'
        elif not password:
            message = 'Password is required.'
        else:
            message = authentication.check_password(username, password)

            if message != "Username doesn't exist." and message != "Password incorrect.":
                session.clear()
                session['user_id'] = message.username
                return redirect(url_for('index.index'))

        flash(message)

    return render_template('auth/login.html')


# Logout page
# Clear session
@blueprint.route('/logout')
def logout():
    session.clear()
    return redirect(url_for('index.index'))


# Only for development
@blueprint.route('/clean')
def clean():
    return authentication.delete_all_user()


# Only for development
@blueprint.route('/list')
def list():
    users = authentication.list_all_user()
    for user in users:
        print(user)
    return "Check terminal for the list of all users."
