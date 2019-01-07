import webbrowser
from flask import Flask, render_template, request, redirect
from api_system import api_page
import api_system

# forms
from forms import PostForm

# markdown handling
import markdown
from flask import Markup
import frontmatter

app = Flask(__name__)
app.register_blueprint(api_page)

# PUT in config later BAD
app.secret_key = b'1234'

# form testing

@app.route('/')
def hello_world():
    return render_template('index.html')

@app.route('/list-posts')
def list_posts():
    posts = api_system.list_posts()

    parsed_posts = []
    for post in posts:
        metadata, content = frontmatter.parse(api_system.get_post_raw(post))

        post_title = post

        if ('Title' in metadata):
            post_title = metadata['Title']

        parsed_posts.append({
            'metadata': metadata,
            'title': post_title,
            'file_name': post,
            'content': content
        })


    return render_template('list_posts.html', posts = parsed_posts)

@app.route('/view-post/<string:post_name>')
def view_post(post_name):
    raw_post_data = api_system.get_post_raw(post_name)
    metadata,content = frontmatter.parse(raw_post_data)
    html_content = Markup(markdown.markdown(content))
    return render_template('view_post.html', post_data = raw_post_data, metadata = metadata, content = html_content)

# TODO get and post requests
@app.route('/new-post', methods=['GET', 'POST'])
def new_post():
    form = PostForm()
    if (request.method == 'GET'):
        return render_template('new_post.html', form = form)
    elif (request.method == 'POST'):
        if form.validate_on_submit():

            # TODO create our post file
            api_system.gen_post(form.title.data, form.content.data, "regular")
            #

            return redirect('/post-success')
        else:
            return redirect('/post-failure')

@app.route('/post-success')
def post_created():
    return render_template('post_created.html')

@app.route('/post-failure')
def post_failed():
    return render_template('post_failed.html')

browser_active = False

if __name__ == "__main__":
    if (browser_active):
        url = 'http://localhost:5000'
        # Open URL in new window, raising the window if possible.
        webbrowser.open_new(url)

    app.run(debug=True)

    #from gevent.pywsgi import WSGIServer
    #http_server = WSGIServer(('', 5000), app)
    #print ("hosting server on port 5000")
    #http_server.serve_forever()
