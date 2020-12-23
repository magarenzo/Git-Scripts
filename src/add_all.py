# Feeling lazy? Quickly run a script in place of manually adding/committing/pushing

from datetime import datetime
import subprocess
import os
from os.path import basename

def current_time() -> str:
    now = datetime.now()
    return now.strftime("%H:%M:%S")

def add_all() -> None:
    project_name = basename(os.getcwd())
    commit_message = "-m Update " + project_name

    subprocess.call(["git"] + ["add", "."])
    subprocess.call(["git"] + ["commit", commit_message])
    subprocess.call(["git"] + ["push"])

# Driver
print(current_time() + " - STARTED - add_all.py")
add_all()
print(current_time() + " - COMPLETED - add_all.py")