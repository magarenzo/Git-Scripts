<# Feeling lazy? Quickly run a script in place of manually adding/committing/pushing #>

Write-Output "$(Get-Date -Format 'HH:mm:ss') - STARTED - Add-All.ps1"

# Add all files
git add .

# Set a simple commit message pertaining to the repo name
$ProjectName = (Get-Location).Path | Split-Path -Leaf
git commit -m "Update $ProjectName"

# Push
git push

Write-Output "$(Get-Date -Format 'HH:mm:ss') - COMPLETED - Add-All.ps1"