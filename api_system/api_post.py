from database.database import db_session
from database.models import Post

import datetime

def list_posts():
    posts = Post.query.all()
    posts_dicts = []
    for post in posts:
        posts_dicts.append(post.__dict__)

    return posts_dicts

# returns formatted posts
def get_formatted_posts():
    posts = list_posts()
    return posts

# TODO retrieves a specific post
def get_post(post_id):
    post = Post.query.get(post_id)
    return post.__dict__

def save_post(title, content):
    # Create the new post
    new_post = Post(title = title, content = content, date = datetime.datetime.now())

    # Add and Save the new post
    db_session.add(new_post)
    db_session.commit()
