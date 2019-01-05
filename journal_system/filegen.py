from datetime import datetime
from string import Template
import sys
import os

JOURNAL_PATH = os.path.dirname(os.path.realpath(__file__))

# Util Function
def uncomplete_date_string(tz=None):
    right_now = datetime.now(tz)
    formatted_time = right_now.strftime("%d-%b-%Y_%H:%M:%S")
    return formatted_time

def general_file_entry_name(entry_name):
    formatted_time_pre = uncomplete_date_string()

    complete_filename = formatted_time_pre + "_" + entry_name
    return complete_filename

class MarkdownJournalGen:

    def __init__(self, working_dir, author):
        self.working_dir = working_dir
        self.author = author

    def create_markdown_entry(self, name, content, template_file_path):
        extension = ".md"
        date_string = uncomplete_date_string()
        template_file = open(template_file_path, 'r')
        template = Template(template_file.read())
        template_text = template.substitute(date = date_string, author = self.author)

        entry_file_name = general_file_entry_name(name) + extension

        f = open(self.working_dir + entry_file_name, "w")
        f.write(template_text + "\n" + content)
        f.close()

    def create_markdown_todo_entry(self, name, content):
        self.create_markdown_entry(name, content, JOURNAL_PATH + '/templates/todo.md')
        pass

    def create_markdown_regular_entry(self, name, content):
        self.create_markdown_entry(name, content, JOURNAL_PATH + '/templates/journal.md')
