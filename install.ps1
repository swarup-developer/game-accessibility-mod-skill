[CmdletBinding(SupportsShouldProcess = $true)]
param(
    [ValidateSet('All', 'Codex', 'Claude', 'Gemini', 'Antigravity', 'Freebuff')]
    [string]$Agent = 'All',
    [ValidateSet('User', 'Project')][string]$Scope = 'User',
    [string]$ProjectPath,
    [string]$UserDirectory = [Environment]::GetFolderPath('UserProfile'),
    [switch]$Interactive,
    [switch]$Uninstall
)
$ErrorActionPreference = 'Stop'
$packageId = 'game-accessibility-mod-skill'

function Assert-Within([string]$Path, [string]$Root) {
    $resolvedPath = [IO.Path]::GetFullPath($Path)
    $resolvedRoot = [IO.Path]::GetFullPath($Root).TrimEnd('\', '/')
    if (-not $resolvedPath.StartsWith($resolvedRoot + [IO.Path]::DirectorySeparatorChar, [StringComparison]::OrdinalIgnoreCase)) {
        throw "Path is outside the selected installation root: $resolvedPath"
    }
    $cursor = $resolvedPath
    while ($cursor -and $cursor.Length -ge $resolvedRoot.Length) {
        if (Test-Path -LiteralPath $cursor) {
            $entry = Get-Item -LiteralPath $cursor -Force
            if (($entry.Attributes -band [IO.FileAttributes]::ReparsePoint) -ne 0) {
                throw "Linked folders are not supported by this installer: $cursor"
            }
        }
        $parent = Split-Path -Parent $cursor
        if ($parent -eq $cursor) { break }
        $cursor = $parent
    }
    return $resolvedPath
}

function Test-Inventory([string]$Folder) {
    $inventoryFile = Join-Path $Folder 'references/inventory.json'
    $inventory = Get-Content -LiteralPath $inventoryFile -Raw | ConvertFrom-Json
    $expected = @('references/inventory.json') + @($inventory.files | ForEach-Object { $_.path })
    foreach ($entry in Get-ChildItem -LiteralPath $Folder -Recurse -Force) {
        if (($entry.Attributes -band [IO.FileAttributes]::ReparsePoint) -ne 0) { throw 'Linked files or folders are not allowed in the skill package.' }
        if (-not $entry.PSIsContainer) {
            $relative = $entry.FullName.Substring($Folder.TrimEnd('\', '/').Length + 1).Replace('\', '/')
            if ($relative -notin $expected) { throw "Unlisted package file: $relative" }
        }
    }
    foreach ($item in $inventory.files) {
        $file = Assert-Within (Join-Path $Folder $item.path) $Folder
        if (-not (Test-Path -LiteralPath $file -PathType Leaf)) { throw "Missing package file: $($item.path)" }
        $stream = [IO.File]::OpenRead($file)
        $hasher = [Security.Cryptography.SHA256]::Create()
        try { $digest = [BitConverter]::ToString($hasher.ComputeHash($stream)).Replace('-', '').ToLowerInvariant() }
        finally { $stream.Dispose(); $hasher.Dispose() }
        if ($digest -ne $item.sha256) {
            throw "Package verification failed: $($item.path). Extract a fresh release before installing."
        }
    }
}

try {
    if ($Interactive) {
        Write-Host 'Game Accessibility Mod Skill'
        Write-Host '1. All supported local assistants (default)'
        Write-Host '2. Codex   3. Claude Code   4. Gemini CLI   5. Antigravity   6. Freebuff CLI'
        $choice = Read-Host 'Choose a number, or press Enter for All'
        $choices = @{ '1' = 'All'; '2' = 'Codex'; '3' = 'Claude'; '4' = 'Gemini'; '5' = 'Antigravity'; '6' = 'Freebuff' }
        if ($choice) {
            if (-not $choices.ContainsKey($choice)) { throw 'Unknown choice. Run the installer again and choose 1 to 6.' }
            $Agent = $choices[$choice]
        }
    }
    $config = Get-Content -LiteralPath (Join-Path $PSScriptRoot 'compatibility.json') -Raw | ConvertFrom-Json
    $name = $config.skill_name
    if ($name -ne 'accessibility-mod-development') { throw 'Unexpected skill name in package configuration.' }
    $source = Join-Path $PSScriptRoot "skills/$name"
    if (-not $Uninstall) { Test-Inventory $source }
    if ($Scope -eq 'Project') {
        if (-not $ProjectPath -or -not (Test-Path -LiteralPath $ProjectPath -PathType Container)) {
            throw 'For a project installation, supply an existing folder with -ProjectPath.'
        }
        $installRoot = [IO.Path]::GetFullPath($ProjectPath)
    } else {
        if (-not $UserDirectory -or -not (Test-Path -LiteralPath $UserDirectory -PathType Container)) { throw 'The user folder does not exist.' }
        $installRoot = [IO.Path]::GetFullPath($UserDirectory)
    }
    $names = if ($Agent -eq 'All') { @('Codex', 'Claude', 'Gemini', 'Antigravity', 'Freebuff') } else { @($Agent) }
    $targets = @($names | ForEach-Object {
        $entry = $config.agents.PSObject.Properties[$_].Value
        $relative = if ($Scope -eq 'User') { $entry.user } else { $entry.project }
        Assert-Within (Join-Path (Join-Path $installRoot $relative) $name) $installRoot
    } | Select-Object -Unique)
    foreach ($target in $targets) {
        $skillsParent = Split-Path -Parent $target
        $agentRoot = Split-Path -Parent $skillsParent
        $stamp = (Get-Date -Format 'yyyyMMdd-HHmmss') + '-' + [Guid]::NewGuid().ToString('N').Substring(0, 8)
        $backup = Assert-Within (Join-Path $agentRoot ".skill-backups/$name/$stamp") $installRoot
        if ($Uninstall) {
            if (-not (Test-Path -LiteralPath $target)) { Write-Host "Not installed: $target"; continue }
            $marker = Join-Path $target '.installation.json'
            if (-not (Test-Path -LiteralPath $marker)) { throw "This folder is not marked as an installation from this package: $target" }
            $receipt = Get-Content -LiteralPath $marker -Raw | ConvertFrom-Json
            if ($receipt.package -ne $packageId) { throw "Different package owns this folder: $target" }
            if ($PSCmdlet.ShouldProcess($target, 'Move installed skill into a backup')) {
                New-Item -ItemType Directory -Path (Split-Path -Parent $backup) -Force | Out-Null
                Move-Item -LiteralPath $target -Destination $backup
                Write-Host "Removed from discovery. Your files are kept at: $backup"
            }
            continue
        }
        if (-not $PSCmdlet.ShouldProcess($target, 'Install verified skill, preserving any existing copy')) { continue }
        New-Item -ItemType Directory -Path $skillsParent -Force | Out-Null
        $staging = Assert-Within (Join-Path $agentRoot ".skill-staging-$stamp") $installRoot
        New-Item -ItemType Directory -Path $staging | Out-Null
        Get-ChildItem -LiteralPath $source -Force | Copy-Item -Destination $staging -Recurse -Force
        Test-Inventory $staging
        @{ package = $packageId; version = (Get-Content -LiteralPath (Join-Path $PSScriptRoot 'VERSION') -Raw).Trim(); installed_utc = [DateTime]::UtcNow.ToString('o') } |
            ConvertTo-Json | Set-Content -LiteralPath (Join-Path $staging '.installation.json') -Encoding UTF8
        $hadBackup = $false
        if (Test-Path -LiteralPath $target) {
            New-Item -ItemType Directory -Path (Split-Path -Parent $backup) -Force | Out-Null
            Move-Item -LiteralPath $target -Destination $backup
            $hadBackup = $true
        }
        try { Move-Item -LiteralPath $staging -Destination $target }
        catch {
            if ($hadBackup -and -not (Test-Path -LiteralPath $target)) { Move-Item -LiteralPath $backup -Destination $target }
            throw
        }
        Write-Host "Installed: $target"
        if ($hadBackup) { Write-Host "Previous copy preserved: $backup" }
    }
    if ($WhatIfPreference) { Write-Host 'Preview finished. No installation changes were made.' }
    else { Write-Host 'Finished. Restart the relevant local assistant and ask it to use accessibility-mod-development.' }
    Write-Host 'Folder placement does not certify model behavior or discovery in every app version.'
} catch {
    Write-Error ("{0}`n{1}" -f $_.Exception.Message, $_.InvocationInfo.PositionMessage) -ErrorAction Continue
    exit 1
}
