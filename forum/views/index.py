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


@blueprint.route('/profile.html')
def profile():
    return render_template('profile.html')


# Search post using keywords
@blueprint.route('/search', methods=('GET', 'POST'))
def search():
    posts = post.list_all_posts()
    if request.method == 'POST':
        keyword = request.form['keyword']

        if not keyword:
            return render_template("index.html", posts=posts)
        else:
            posts = post.search_by_keyword(keyword)
            return render_template("index.html", posts=posts)

    return render_template("index.html", posts=posts)
