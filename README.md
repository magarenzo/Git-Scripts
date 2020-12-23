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

## Running the Scripts

1. Open a PowerShell session

2. Optionally run the following to allow the current session to run scripts not digitally signed:

    ```powershell
    Set-ExecutionPolicy -Scope Process -ExecutionPolicy Bypass
    ```

3. Run one of the following scripts from within the repo you are updating (it does not matter if the script itself is located in a different directory):

### Add-All.ps1

* Run the following to add all files, set a simple commit message pertaining to the repo name, and push:

```powershell
.\Add-All.ps1
```

## TODO

### Add-Per-File.ps1

* Run the following to add all files, set a simple commit message per file pertaining to that file's name, and push:

```powershell
.\Add-Per-File.ps1
```

## Owner

[Michael A. Agarenzo](https://magarenzo.com)
