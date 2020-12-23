from datetime import datetime
#import subprocess

# Feeling lazy? Quickly run a script in place of manually adding/committing/pushing

def current_time() -> str:
    now = datetime.now()
    return str(now.strftime("%H:%M:%S"))

# TODO
def add_per_file() -> None:
    print("TODO")

# Driver
print(current_time() + " - STARTED - add_per_file.py")
add_per_file()
print(current_time() + " - COMPLETED - add_per_file.py")