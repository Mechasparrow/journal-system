import json
import os

def load_config():
    f = open('./_config/config.json', 'r')
    read_data = f.read()
    json_data = json.loads(read_data)

    return {
        'working_dir': json_data['working_dir'],
        'author': json_data['author']
    }
