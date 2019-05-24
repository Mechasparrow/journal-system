import json
import os
import frontmatter

from journal_system import MarkdownJournalGen

def load_config():
    f = open('./_config/config.json', 'r')
    read_data = f.read()
    json_data = json.loads(read_data)

    return {
        'working_dir': json_data['working_dir'],
        'author': json_data['author']
    }

config = load_config()

def list_posts():
    path = config['working_dir']
    arr = os.listdir(path)
    selected_documents = list(filter(lambda file: file.endswith('.md'), arr))
    return selected_documents

# returns formatted posts
def get_formatted_posts():

    posts = list_posts()

    parsed_posts = []
    for post in posts:
        metadata, content = frontmatter.parse(get_post_raw(post))

        post_title = post

        if ('Title' in metadata):
            post_title = metadata['Title']

        parsed_posts.append({
            'metadata': metadata,
            'title': post_title,
            'file_name': post,
            'content': content
        })

    return parsed_posts

def get_post_raw(post_file):
    try:
        post_file_path = config['working_dir'] + '/' + post_file
        f = open(post_file_path)
        post_data = f.read()

        return post_data
    except FileNotFoundError:
        return None

def gen_post_empty(doc_name, type):
    gen_post(doc_name, "", type)

# TODO generate the post with some options
def gen_post(doc_name, content, type):
    mdJg = MarkdownJournalGen(config['working_dir'], config['author'])
    what_kind = type
    entry_name = doc_name

    if (what_kind == 'todo'):
        mdJg.create_markdown_todo_entry(entry_name, content)
        pass
    else:
        mdJg.create_markdown_regular_entry(entry_name, content)
        pass


        print ("entry created at " + config['working_dir'])
