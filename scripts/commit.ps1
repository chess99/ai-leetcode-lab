param(
    [Parameter(Mandatory = $true)]
    [string] $Message,

    [Parameter(Mandatory = $true)]
    [string[]] $Paths
)

$ErrorActionPreference = "Stop"
$repoRoot = (git rev-parse --show-toplevel 2>$null).Trim()
if (-not $repoRoot) {
    throw "当前目录不在 Git 仓库中。"
}
Set-Location -LiteralPath $repoRoot

$alreadyStaged = @(git diff --cached --name-only)
if ($alreadyStaged.Count -gt 0) {
    throw "暂存区已有内容，为避免混入他人修改，本次提交已停止。"
}

foreach ($path in $Paths) {
    if (-not (Test-Path -LiteralPath $path -PathType Leaf)) {
        throw "只接受明确存在的文件路径：$path"
    }
}

& git add -- @Paths
if ($LASTEXITCODE -ne 0) {
    throw "git add 失败。"
}

$staged = @(git diff --cached --name-only)
if ($staged.Count -eq 0) {
    throw "没有可提交的变更。"
}

git diff --staged --check
if ($LASTEXITCODE -ne 0) {
    throw "暂存内容存在空白或冲突问题。"
}

git diff --staged
& git commit -m $Message
exit $LASTEXITCODE
