from datetime import datetime
import subprocess

# Feeling lazy? Quickly run a script in place of manually adding/committing/pushing

def current_time() -> str:
    now = datetime.now()
    return str(now.strftime("%H:%M:%S"))

def add_all() -> None:
    subprocess.run("git add .")
    subprocess.run("git commit -m \"Test\"")
    subprocess.run("git push")

# Driver
print(current_time() + " - STARTED - add_all.py")
add_all()
print(current_time() + " - COMPLETED - add_all.py")