from filegen import MarkdownJournalGen

from config import *

def test():

    pass

def run():
    entry_name = input("Pick a name for the journal entry: ")
    mdJg = MarkdownJournalGen(WORKING_DIR, AUTHOR)
    mdJg.create_markdown_entry(entry_name)
    print ("entry created at " + WORKING_DIR)


if __name__ == "__main__":
    run()
