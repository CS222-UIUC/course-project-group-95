from flask import flash, redirect, render_template, request, Blueprint, url_for

from models import *
from app import app

blueprint = Blueprint('view', __name__)


@app.route('/hello')
def hello():
    return 'Hello, World!'


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/notification.html')
def notification():
    return render_template('notification.html')


@app.route('/profile.html')
def profile():
    return render_template('profile.html')


@app.route('/search.html')
def search():
    return render_template('search.html')


@app.route('/register.html', methods=('GET', 'POST'))
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
                create_user(username, password)
                return redirect(url_for('login'))
            except:
                message = 'Username exists.'

        flash(message)

    return render_template('auth/register.html')


@app.route('/login.html', methods=('GET', 'POST'))
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


@app.route('/register/clean')
def clean():
    return delete_all_user()


@app.route('/list')
def list():
    users = list_all_user()
    for user in users:
        print(user)
    return "Check terminal for the list of all users."
