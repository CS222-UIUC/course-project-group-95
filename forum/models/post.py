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


# Upvote post
def upvote_post(user_id, post_id):
    tz = pytz.timezone('US/Central')
    cur_time = datetime.now(tz=tz)
    upvote = models.Upvote(user_id, post_id, cur_time)
    db.session.add(upvote)
    db.session.commit()


# Unupvote post
def unupvote_post(user_id, post_id):
    models.Upvote.query.filter_by(user_id=user_id, post_id=post_id).delete()
    db.session.commit()


# Check if user has upvoted the post
def check_upvoted(user_id, post_id):
    upvoted = models.Upvote.query.filter_by(
        user_id=user_id, post_id=post_id).all()
    return len(upvoted) == 1


# Get the number of upvotes of the post
def get_upvote_num(post_id):
    return len(models.Upvote.query.filter_by(post_id=post_id).all())


# Favourite post
def favourite_post(user_id, post_id):
    tz = pytz.timezone('US/Central')
    cur_time = datetime.now(tz=tz)
    favourite = models.Favourite(user_id, post_id, cur_time)
    db.session.add(favourite)
    db.session.commit()


# Unfavourite post
def unfavourite_post(user_id, post_id):
    models.Favourite.query.filter_by(user_id=user_id, post_id=post_id).delete()
    db.session.commit()


# Check if user has favourited the post
def check_favourited(user_id, post_id):
    favourited = models.Favourite.query.filter_by(
        user_id=user_id, post_id=post_id).all()
    return len(favourited) == 1


# Get all favourites of the user
def get_all_favoutites(user_id):
    return db.session.query(models.Favourite, models.Post).filter_by(user_id=user_id).join(models.Post).order_by(models.Favourite.time.desc()).all()


# Get the total number of upvotes a user get
def get_user_upvote_num(user_id):
    upvotes = db.session.query(models.Upvote, models.Post).join(
        models.Post).filter_by(author=user_id).all()
    return len(upvotes)


# Create new reply for the given post
def create_reply(post_id, reply_id, author, content):
    tz = pytz.timezone('US/Central')
    cur_time = datetime.now(tz=tz)
    reply = models.Reply(post_id, reply_id, author, content, cur_time)
    db.session.add(reply)
    db.session.commit()


# Get all reply for the given post_id
def get_reply(post_id):
    return models.Reply.query.filter_by(post_id=post_id).order_by(models.Reply.time).all()
