# Git Scripts

Feeling lazy? Quickly run a script in place of manually adding/committing/pushing

## Overview

I find that I'm often running the same set of Git commands when I'm updating a(n unimportant) project and have nothing specific to put in the commit messages for the changes I made:

```powershell
git add .
git commit -m "Update ProjectName"
git push
```

This prompted me to want to spin up some really simple Git scripts for a few different scenarios I often find myself in

Keep in mind that you may need to run the following to allow your current PowerShell session to run PowerShell scripts not digitally signed:

```powershell
Set-ExecutionPolicy -Scope Process -ExecutionPolicy Bypass
```

## Running the Scripts

Run one of the following scripts from within the root of the repo you are updating (it does not matter if the script itself is located in a different directory):

### Add All

* Run either of the following to add all files, set a simple commit message pertaining to the repo name, and push:

#### Add-All.ps1

```powershell
.\Add-All.ps1
```

#### add_all.py

```python
python add_all.py
```

## TODO

### Add Per File

* Run either of the following to add all files one at a time, set a simple commit message per file pertaining to that file's name, and push:

#### Add-Per-File.ps1

```powershell
.\Add-Per-File.ps1
```

#### add_per_file.py

```python
python add_per_file.py
```

## Owner

[Michael A. Agarenzo](https://magarenzo.com)
