from flask import flash, redirect, render_template, request, Blueprint, url_for, session
from ..models import authentication
from sqlalchemy import exc


# Register blueprint
blueprint = Blueprint('view', __name__)


@blueprint.route('/hello')
def hello():
    return 'Hello, World!'


@blueprint.route('/')
def index():
    return render_template('index.html')


@blueprint.route('/notification.html')
def notification():
    return render_template('notification.html')


@blueprint.route('/profile.html')
def profile():
    return render_template('profile.html')


@blueprint.route('/search.html')
def search():
    return render_template('search.html')


# Register page:
# Flash warning messages when username or password is not given or when username already exists
# Redirect to login page if registered successfully
@blueprint.route('/register.html', methods=('GET', 'POST'))
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
                return redirect(url_for('view.login'))
            except exc.IntegrityError:
                message = 'Username exists.'

        flash(message)

    return render_template('auth/register.html')


# Login page:
# Flash warning messages when username or password is not given
#                       or when username and password doesn't match
# Redirect to index page and register user in session if logged in successfully
@blueprint.route('/login.html', methods=('GET', 'POST'))
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
                return redirect(url_for('view.index'))

        flash(message)

    return render_template('auth/login.html')


# Logout page
# Clear session
@blueprint.route('/logout')
def logout():
    session.clear()
    return redirect(url_for('view.index'))


# Only for development
@blueprint.route('/register/clean')
def clean():
    return authentication.delete_all_user()


# Only for development
@blueprint.route('/list/all_users')
def list():
    users = authentication.list_all_user()
    for user in users:
        print(user)
    return "Check terminal for the list of all users."
