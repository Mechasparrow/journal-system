from datetime import datetime

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

    def create_markdown_entry(self, name):
        extension = ".md"
        date_string = uncomplete_date_string()
        template_text = '''---\n''' + "Date: " + date_string + "\n" + "Author: " + self.author + "\n" + '''---\n'''

        entry_file_name = general_file_entry_name(name) + extension

        f = open(self.working_dir + entry_file_name, "w")
        f.write(template_text)
        f.close()