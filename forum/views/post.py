from flask import flash, redirect, render_template, request, Blueprint, url_for, session
from ..models import authentication, post
from sqlalchemy import exc


# Register blueprint
blueprint = Blueprint('post', __name__, url_prefix='/post/')


@blueprint.route('/edit')
def edit_post():
    return "edit post"


@blueprint.route('/view')
def view_post():
    id = request.args.to_dict()['id']
    return render_template("post/post.html", post=post.get_post(id))


@blueprint.route('/create', methods=('GET', 'POST'))
def create_post():
    if request.method == 'POST':
        title = request.form['title']
        content = request.form['content']
        message = None

        if not title:
            message = 'Title is required.'
        else:
            # try:
            post.create_post(title, content, session.get('user_id'))
            return redirect(url_for('index.index'))
            # except:

        flash(message)

    return render_template("post/create_post.html")
