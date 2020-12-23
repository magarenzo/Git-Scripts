# Feeling lazy? Quickly run a script in place of manually adding/committing/pushing

from datetime import datetime
import subprocess

def current_time() -> str:
    now = datetime.now()
    return now.strftime("%H:%M:%S")

# TODO: Implement add_per_file()
def add_per_file() -> None:
    print("TODO")

# Driver
print(current_time() + " - STARTED - add_per_file.py")
add_per_file()
print(current_time() + " - COMPLETED - add_per_file.py")