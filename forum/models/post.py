from datetime import datetime
from . import models
from ..db import db
import pytz


# Return all posts in the database
def list_all_posts():
    return models.Post.query.order_by(models.Post.create_datetime.desc())


# Get post by id
def get_post(id):
    return models.Post.query.filter_by(id=id).one()


# Create a new post using the title, content, and author_id parameters
def create_post(title, content, user_id):
    tz = pytz.timezone('US/Central')
    cur_time = datetime.now(tz=tz)
    new_post = models.Post(title, user_id, cur_time, content)

    db.session.add(new_post)
    db.session.commit()

    return new_post


# Update the post with id as post_id using new title and content
def update_post(title, content, id):
    models.Post.query.filter_by(id=id).update(
        {'title': title, 'content': content})
    db.session.commit()


# Delete the post with id as post_id
def delete_post(id):
    models.Post.query.filter_by(id=id).delete()
    db.session.commit()


# Delete all post
def delete_all_post():
    models.Post.query.delete()
    db.session.commit()


# Search post by keyword,
# keyword could be part of the post's title, content, or author
def search_post_by_keyword(keyword):
    search = "%{}%".format(keyword)
    posts = models.Post.query.filter(models.Post.title.like(search)).union(
        models.Post.query.filter(models.Post.content.like(search))).union(
            models.Post.query.filter(models.Post.author.like(search))).order_by(
                models.Post.create_datetime.desc()).all()
    return posts
