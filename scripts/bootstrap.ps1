$ErrorActionPreference = "Stop"
$repoRoot = Split-Path -Parent $PSScriptRoot
Set-Location -LiteralPath $repoRoot

if (-not (Get-Command python -ErrorAction SilentlyContinue)) {
    throw "需要 Python 3.11 或更高版本。"
}

if (-not (Test-Path -LiteralPath ".git")) {
    git init --initial-branch=main
}

New-Item -ItemType Directory -Force -Path ".secrets", ".ai", ".runtime" | Out-Null
if (-not (Test-Path -LiteralPath ".secrets\leetcode.env")) {
    Copy-Item -LiteralPath ".env.example" -Destination ".secrets\leetcode.env"
    Write-Host "已创建 .secrets\leetcode.env，请填入专用账号凭证。"
}
if (-not (Test-Path -LiteralPath ".ai\identity.env")) {
    Copy-Item -LiteralPath ".ai\identity.env.example" -Destination ".ai\identity.env"
    Write-Host "已创建 .ai\identity.env，请填入当前 AI 客户端与模型。"
}

git config core.hooksPath .githooks
python -m unittest discover -s tests -p "test_*.py" -v
Write-Host "环境初始化完成。下一步运行 .\ai-lc.ps1 doctor"
