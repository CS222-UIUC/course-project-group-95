from flask import render_template, request, Blueprint
from ..models import post


# Register blueprint
blueprint = Blueprint('index', __name__)


# Route for the index page
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
            posts = post.search_post_by_keyword(keyword)
            return render_template("index.html", posts=posts)

    return render_template("index.html", posts=posts)
