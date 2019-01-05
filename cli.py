from journal_system import MarkdownJournalGen
import json

def test():
    d = load_config()

def load_config():

    f = open('./_config/config.json', 'r')
    read_data = f.read()
    json_data = json.loads(read_data)

    return {
        'working_dir': json_data['working_dir'],
        'author': json_data['author']
    }

def run():
    entry_name = input("Pick a name for the journal entry: ")
    config = load_config()
    mdJg = MarkdownJournalGen(config['working_dir'], config['author'])

    what_kind = input("What kind of entry: (regular, todo): ")

    if (what_kind == 'todo'):
        mdJg.create_markdown_todo_entry(entry_name, content = "")
    else:
        mdJg.create_markdown_regular_entry(entry_name, content = "")

    print ("entry created at " + config['working_dir'])


if __name__ == "__main__":
    run()
    #test()
