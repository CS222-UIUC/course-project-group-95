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


def create_post(title, content, user_id):
    tz = pytz.timezone('US/Central')
    cur_time = datetime.now(tz=tz)
    new_post = models.Post(title, user_id, cur_time, content)

    db.session.add(new_post)
    db.session.commit()

    return new_post
