# Feeling lazy? Quickly run a script in place of manually adding/committing/pushing

from datetime import datetime
import subprocess

# Return current_time
def current_time() -> str:
    now = datetime.now()
    return now.strftime("%H:%M:%S")

# Add all files
# Set a simple commit message per file pertaining to that file's name
# Push
def add_per_file() -> None:
    print("TODO: Implement add_per_file()")

# Driver
print(current_time() + " - STARTED - add_per_file.py")
add_per_file()
print(current_time() + " - COMPLETED - add_per_file.py")