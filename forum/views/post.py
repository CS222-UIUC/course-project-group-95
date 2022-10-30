from flask import flash, redirect, render_template, request, Blueprint, url_for, session
from ..models import authentication, post
from sqlalchemy import exc


# Register blueprint
blueprint = Blueprint('post', __name__, url_prefix='/post/')


# Edit post page for given post_id
@blueprint.route('/edit', methods=('GET', 'POST'))
def edit_post():
    id = request.args.to_dict()['id']
    if request.method == 'POST':
        title = request.form['title']
        content = request.form['content']
        message = None

        if not title:
            message = 'Title is required.'
        else:
            # try:
            post.update_post(title, content, id)
            return redirect(url_for('index.index'))
            # except:

        flash(message)
    return render_template("post/edit_post.html", post=post.get_post(id))


# View post page
# If session user equals to author, button for delete and edit will be shown
@blueprint.route('/view')
def view_post():
    id = request.args.to_dict()['id']
    return render_template("post/post.html", post=post.get_post(id))


# Delete post page, redirects to index page
@blueprint.route('/delete')
def delete_post():
    id = request.args.to_dict()['id']
    post.delete_post(id)
    return redirect(url_for('index.index'))


# Create post page
@blueprint.route('/create', methods=('GET', 'POST'))
def create_post():
    if request.method == 'POST':
        title = request.form['title']
        content = request.form['content']
        message = None

        if not title:
            message = 'Title is required.'
        else:
            post.create_post(title, content, session.get('user_id'))
            return redirect(url_for('index.index'))

        flash(message)

    return render_template("post/create_post.html")
