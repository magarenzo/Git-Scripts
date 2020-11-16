<# Feeling lazy? Quickly run a script in place of manually adding/committing/pushing #>

$ProjectName = (Get-Location).Path | Split-Path -Leaf

Write-Output "$(Get-Date -Format 'HH:mm:ss') - STARTED - Add-All.ps1"

git add .
git commit -m "Update $ProjectName"
git push

Write-Output "$(Get-Date -Format 'HH:mm:ss') - COMPLETED - Add-All.ps1"