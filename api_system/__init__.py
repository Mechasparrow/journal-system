from flask import Blueprint, render_template, abort, request, jsonify
from jinja2 import TemplateNotFound

from .api_util import *

api_page = Blueprint("api_system", __name__, template_folder = '../templates')

@api_page.route('/api/get_docs')
def get_docs():
    documents = list_posts()
    return jsonify(docs = documents)

@api_page.route('/api/get_doc/<string:postname>')
def get_doc(postname):
    post_data = get_post_raw(postname)

    if (post_data):
        return jsonify(status = 200, post_text = post_data)
    else:
        return jsonify(status = 404, error = "File not found")

@api_page.route('/api/new_doc', methods = ['POST'])
def new_doc():
    if request.method == 'POST':
        json_data = request.get_json()
        if (json_data.get('title', None) and json_data.get('type', None)):
            gen_post(json_data.get('title'), json_data.get('type'))
            return jsonify(status = 200, result = "post generated")
        else:
            return jsonify(status = 404, result = "post unable to be generated")
