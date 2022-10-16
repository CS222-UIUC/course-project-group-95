from flask import flash, redirect, render_template, request, Blueprint, url_for
from ..models import authentication
from sqlalchemy import exc


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
        # else:
        # Todo: Implement database query, save user id for use in other pages

        flash(message)

    return render_template('auth/login.html')


@blueprint.route('/register/clean')
def clean():
    return authentication.delete_all_user()


@blueprint.route('/list/all_users')
def list():
    users = authentication.list_all_user()
    for user in users:
        print(user)
    return "Check terminal for the list of all users."
