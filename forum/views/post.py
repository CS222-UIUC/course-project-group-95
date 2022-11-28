from flask import flash, redirect, render_template, request, Blueprint, url_for, session
from ..models import post


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
    return render_template("post/post.html", post=post.get_post(id),
                           upvote_num=post.get_upvote_num(id),
                           upvoted=post.check_upvoted(
                               session.get('user_id'), id),
                           favourited=post.check_favourited(session.get('user_id'), id))


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


# Upvote post
@blueprint.route('/upvote', methods=('GET', 'POST'))
def upvote():
    id = request.args.to_dict()['id']
    post.upvote_post(session.get('user_id'), id)
    return redirect(url_for('post.view_post', id=id))


# Unupvote post
@blueprint.route('/unupvote', methods=('GET', 'POST'))
def unupvote():
    id = request.args.to_dict()['id']
    post.unupvote_post(session.get('user_id'), id)
    return redirect(url_for('post.view_post', id=id))


# Favourite post
@blueprint.route('/favourite', methods=('GET', 'POST'))
def favourite():
    id = request.args.to_dict()['id']
    post.favourite_post(session.get('user_id'), id)
    return redirect(url_for('post.view_post', id=id))


# Unfavourite post
@blueprint.route('/unfavourite', methods=('GET', 'POST'))
def unfavourite():
    id = request.args.to_dict()['id']
    post.unfavourite_post(session.get('user_id'), id)
    return redirect(url_for('post.view_post', id=id))
