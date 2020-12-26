<# Feeling lazy? Quickly run a script in place of manually adding/committing/pushing #>

Write-Output "$(Get-Date -Format 'HH:mm:ss') - STARTED - Add-Per-File.ps1"

# Add all files
git add .

# Set a simple commit message per file pertaining to that file's name
$FileList = git diff --cached --name-only
$FileCount = $FileList.count
if ($FileCount -gt 1) {
    for ($GitFile = 0; $GitFile -lt $FileCount; $GitFile++) {
        git commit -m $FileList[$GitFile]
    }
} else {
    Write-Output "this -> $FileList"
    git commit -m "Update $FileList"
}

# Push
# git push

Write-Output "$(Get-Date -Format 'HH:mm:ss') - COMPLETED - Add-Per-File.ps1"