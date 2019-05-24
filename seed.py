from database.database import db_session
from database.models import Post
from datetime import datetime

from api_system import get_formatted_posts

# correctly parses the post to a Post Object
def parse_post(post):
    # parse into datetime object
    # EX 21-May-2019_21:24:15
    datetime_obj = datetime.strptime(post["metadata"]["Date"], '%d-%b-%Y_%H:%M:%S')
    markdown_content = post["content"]
    title = post["title"]

    ## Debug
    '''
    print ("Title: " + title)
    print ("Date: " + str(datetime_obj))
    print ("Content: " + markdown_content)
    '''

    new_post = Post(title = title, content = markdown_content, date = datetime_obj)
    return new_post

# Delete current
db_session.query(Post).delete()

# Seeding code

# TODO grab all the posts
posts = get_formatted_posts()

# TODO Iterate through each and push it to the database
for post in posts:
    parsed_post = parse_post(post)
    db_session.add(parsed_post)

# Commit to db
db_session.commit()

# Show new Posts
Post.query.all()

# End db code
db_session.remove()
