import webbrowser
from flask import Flask, render_template
from api_system import api_page
import api_system

import markdown
from flask import Markup
import frontmatter

app = Flask(__name__)
app.register_blueprint(api_page)

@app.route('/')
def hello_world():
    return render_template('index.html')

@app.route('/list-posts')
def list_posts():
    posts = api_system.list_posts()
    return render_template('list_posts.html', posts = posts)

@app.route('/view-post/<string:post_name>')
def view_post(post_name):
    raw_post_data = api_system.get_post_raw(post_name)
    metadata,content = frontmatter.parse(raw_post_data)
    html_content = Markup(markdown.markdown(content))
    return render_template('view_post.html', post_data = raw_post_data, metadata = metadata, content = html_content)

# TODO get and post requests
@app.route('/new-post')
def new_post():
    return render_template('new_post.html')

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
