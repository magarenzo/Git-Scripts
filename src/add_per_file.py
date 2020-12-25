# Feeling lazy? Quickly run a script in place of manually adding/committing/pushing

from datetime import datetime
import subprocess
import os
from os.path import basename

# Return current_time
def current_time() -> str:
    now = datetime.now()
    return now.strftime("%H:%M:%S")

# Add all files
# Set a simple commit message per file pertaining to that file's name
# Push
def add_per_file() -> None:
    project_name = basename(os.getcwd())
    subprocess.call(["git"] + ["add", "."])

    file_list = subprocess.check_output(["git"] + ["diff"] + ["--cached"] + ["--name-only"], text=True).split("\n")[:-1]
    for file in file_list:
        commit_message = "Update " + file + " in " + project_name
        filepath = "./" + file
        subprocess.call(["git"] + ["commit", "-m", commit_message] + [filepath])

    subprocess.call(["git"] + ["push"])

# Driver
print(current_time() + " - STARTED - add_per_file.py")
add_per_file()
print(current_time() + " - COMPLETED - add_per_file.py")