# Imports
import os
import shutil
from api_system import api_util

# Get the config
config = api_util.load_config()

# File config
filenamesrc = "data.db"
filenamedest = "journal.db"
srcdest = os.path.abspath("./database") + "/" + filenamesrc
targetdest = config['working_dir'] + filenamedest

# Delete the file if it already exists
if os.path.isfile(targetdest):
    os.remove(targetdest)
else:
    print ("No preexisting database found")

# Copy file to dest
shutil.copyfile(srcdest, targetdest)

print ("Backed Up")
