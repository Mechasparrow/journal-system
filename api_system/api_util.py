import json
import os

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

def get_post_raw(post_file):
    try:
        post_file_path = config['working_dir'] + '/' + post_file
        f = open(post_file_path)
        post_data = f.read()

        return post_data
    except FileNotFoundError:
        return None

# TODO generate the post with some options
def gen_post(doc_name, type):
    mdJg = MarkdownJournalGen(config['working_dir'], config['author'])
    what_kind = type
    entry_name = doc_name

    if (what_kind == 'todo'):
        mdJg.create_markdown_todo_entry(entry_name)
        pass
    else:
        mdJg.create_markdown_regular_entry(entry_name)
        pass

    print ("entry created at " + config['working_dir'])
