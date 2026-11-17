[CmdletBinding()]
param([string]$Owner)
$ErrorActionPreference = 'Stop'
$packageRoot = Split-Path -Parent $PSScriptRoot
Set-Location -LiteralPath $packageRoot

function Check-Exit([string]$Message) {
    if ($LASTEXITCODE -ne 0) { throw $Message }
}

$loginResult = gh api user --jq .login
Check-Exit 'Sign in to GitHub CLI with gh auth login, then run this script again.'
$login = $loginResult.Trim()
if (-not $Owner) { $Owner = $login }
if ($Owner -ne $login) { throw 'This release script creates a personal repository only. Owner must match the signed-in account.' }
python scripts/package.py validate
Check-Exit 'Package validation failed.'
python scripts/package.py build
Check-Exit 'Release build failed.'

if (-not (Test-Path -LiteralPath (Join-Path $packageRoot '.git'))) {
    git init --initial-branch=main $packageRoot
    Check-Exit 'Could not initialize the standalone repository.'
}
$gitRoot = (git rev-parse --show-toplevel).Trim()
Check-Exit 'Could not identify the local repository.'
if ([IO.Path]::GetFullPath($gitRoot) -ne [IO.Path]::GetFullPath($packageRoot)) { throw 'Refusing to publish a parent or unrelated repository.' }
if (git remote) { throw 'A remote already exists. Inspect it and publish manually to avoid changing an existing repository.' }
git add -- .
Check-Exit 'Could not stage release files.'
git commit -m 'Publish portable game accessibility mod development skill'
Check-Exit 'Could not create the initial commit.'
$repository = "$Owner/game-accessibility-mod-skill"
gh repo create $repository --public --source $packageRoot --remote origin --push --description 'Portable accessibility mod development skill with verified controls, research helpers, and a Windows installer'
Check-Exit 'Repository creation or push failed. Inspect the remote before retrying.'
$version = (Get-Content VERSION -Raw).Trim()
$files = @((Resolve-Path "dist/game-accessibility-mod-skill-$version.zip").Path, (Resolve-Path "dist/accessibility-mod-development-$version.skill.zip").Path, (Resolve-Path 'dist/SHA256SUMS.txt').Path)
gh release create "v$version" @files --repo $repository --target main --title "Game Accessibility Mod Skill $version" --notes-file RELEASE_NOTES.md
Check-Exit 'Source is published, but the release upload did not complete.'
Write-Host "Published: https://github.com/$repository/releases/tag/v$version"
