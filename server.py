# Flask lib
from flask import Flask, render_template, request, redirect
import webbrowser

# Math lib
import math

# Database handling
from database.database import db_session

# API
import api_system.api_post as api_post
import api_system.api_util as api_util

# forms
from forms import PostForm

# markdown handling
from flask import Markup
import markdown
import frontmatter


app = Flask(__name__)

# Load in config
app.config.from_envvar('JOURNAL_SETTINGS')

# Home route
@app.route('/')
def home():
    # Profile data
    profile_data = api_util.load_config()

    profile = {
        'name': profile_data['author']
    }

    # Post data
    formatted_posts = api_post.get_formatted_posts()

    #NOTE may need to filter by date first
    recent_posts = formatted_posts[0:3]

    return render_template('index.html', recent_posts = recent_posts, profile = profile)

# Post List route
@app.route('/list-posts/', defaults = {'page': 1})
@app.route('/list-posts/<int:page>')
def list_posts(page):
    # Retrieve formatted posts
    parsed_posts = api_post.get_formatted_posts()

    # NOTE Can be modified later

    # represents amount of posts per page
    amnt_per_page = 5

    # Pages to show centered around the active page
    pages_to_show = 2

    # total posts
    post_count = len(parsed_posts)

    # amount of pages
    page_count = math.ceil(post_count/amnt_per_page)

    if (page != 0):
        starting_page_index = (page - 1) * amnt_per_page
        ending_page_index = starting_page_index + amnt_per_page
        page_posts = parsed_posts[starting_page_index: ending_page_index]
    else:
        page_posts = parsed_posts

    # Render the template
    return render_template('list_posts.html', pages = page_count, current_page = page, pages_to_show = pages_to_show, posts = page_posts)

# View specific post
@app.route('/view-post/<int:post_id>')
def view_post(post_id):
    retrieved_post = api_post.get_post(post_id)
    print(retrieved_post)

    # TODO retrieve post content
    content = retrieved_post['content']

    html_content = Markup(markdown.markdown(content))
    return render_template('view_post.html', post_data = retrieved_post, content = html_content)

# Create and Submit Posts
@app.route('/new-post', methods=['GET', 'POST'])
def new_post():
    form = PostForm()
    if (request.method == 'GET'):
        return render_template('new_post.html', form = form)
    elif (request.method == 'POST'):
        if form.validate_on_submit():

            # create our post file
            api_post.save_post(form.title.data, form.content.data)

            return redirect('/post-success')
        else:
            return redirect('/post-failure')

# Success and failure pages
@app.route('/post-success')
def post_created():
    return render_template('post_created.html')

@app.route('/post-failure')
def post_failed():
    return render_template('post_failed.html')

# When the server goes down, disconnect from the database session
@app.teardown_appcontext
def shutdown_session(exception=None):
    db_session.remove()

# If server script ran individually
if __name__ == "__main__":
    app.run()
