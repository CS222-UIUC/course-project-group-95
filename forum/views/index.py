from flask import flash, redirect, render_template, request, Blueprint, url_for, session
from ..models import authentication, post
from sqlalchemy import exc


# Register blueprint
blueprint = Blueprint('index', __name__)


@blueprint.route('/')
def index():
    posts = post.list_all_posts()
    return render_template('index.html', posts=posts)


@blueprint.route('/hello')
def hello():
    return 'Hello, World!'


@blueprint.route('/notification.html')
def notification():
    return render_template('notification.html')


@blueprint.route('/profile.html')
def profile():
    return render_template('profile.html')


@blueprint.route('/search.html')
def search():
    return render_template('search.html')
