from flask import Flask, render_template
from api_system import api_page

app = Flask(__name__)
app.register_blueprint(api_page)

@app.route('/')
def hello_world():
    return render_template('index.html')

if __name__ == "__main__":
    app.run(debug=True)
    #from gevent.pywsgi import WSGIServer
    #http_server = WSGIServer(('', 5000), app)
    #print ("hosting server on port 5000")
    #http_server.serve_forever()
