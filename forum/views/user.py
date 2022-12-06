from flask import flash, redirect, render_template, request, Blueprint, url_for, session
from ..models import authentication
from ..models.post import get_all_favoutites, get_user_upvote_num


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
            all_users = authentication.list_all_user()
            username_exist = False
            for user in all_users:
                if username == user.username:
                    username_exist = True
            if username_exist:
                message = 'Username exists.'
            else:
                authentication.create_user(username, password)
                return redirect(url_for('user.login'))

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


# Delete all users
@blueprint.route('/clean')
def clean():
    return authentication.delete_all_user()


# List all users
@blueprint.route('/list')
def list():
    users = authentication.list_all_user()
    user_list = []
    for user in users:
        user_list.append(user.username)
    return user_list


# Profile page
@blueprint.route('/profile')
def profile():
    posts = get_all_favoutites(session.get('user_id'))
    num_upvote = get_user_upvote_num(session.get('user_id'))
    return render_template('profile.html', posts=posts, num_upvote=num_upvote)
