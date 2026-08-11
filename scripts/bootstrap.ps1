$ErrorActionPreference = "Stop"
$repoRoot = Split-Path -Parent $PSScriptRoot
Set-Location -LiteralPath $repoRoot

if (-not (Get-Command python -ErrorAction SilentlyContinue)) {
    throw "Python 3.11 or newer is required."
}

if (-not (Test-Path -LiteralPath ".git")) {
    git init --initial-branch=main
}

New-Item -ItemType Directory -Force -Path ".secrets", ".ai", ".runtime" | Out-Null
if (-not (Test-Path -LiteralPath ".secrets\leetcode.env")) {
    Copy-Item -LiteralPath ".env.example" -Destination ".secrets\leetcode.env"
    Write-Host "Created .secrets\leetcode.env; add the dedicated account credentials."
}
if (-not (Test-Path -LiteralPath ".ai\identity.env")) {
    Copy-Item -LiteralPath ".ai\identity.env.example" -Destination ".ai\identity.env"
    Write-Host "Created .ai\identity.env; add the current AI client and model."
}

git config core.hooksPath .githooks
python -m unittest discover -s tests -p "test_*.py" -v
Write-Host "Bootstrap complete. Next: .\ai-lc.ps1 doctor"
