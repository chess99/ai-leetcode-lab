param(
    [Parameter(Mandatory = $true)]
    [string] $Message,

    [Parameter(Mandatory = $true)]
    [string[]] $Paths
)

$ErrorActionPreference = "Stop"
$repoRoot = (git rev-parse --show-toplevel 2>$null).Trim()
if (-not $repoRoot) {
    throw "The current directory is not inside a Git repository."
}
Set-Location -LiteralPath $repoRoot

$alreadyStaged = @(git diff --cached --name-only)
if ($alreadyStaged.Count -gt 0) {
    throw "The staging area is not empty; refusing to mix unrelated changes."
}

foreach ($path in $Paths) {
    if (-not (Test-Path -LiteralPath $path -PathType Leaf)) {
        throw "Only explicit existing file paths are accepted: $path"
    }
}

& git add -- @Paths
if ($LASTEXITCODE -ne 0) {
    throw "git add failed."
}

$staged = @(git diff --cached --name-only)
if ($staged.Count -eq 0) {
    throw "There are no changes to commit."
}

git diff --staged --check
if ($LASTEXITCODE -ne 0) {
    throw "The staged diff contains whitespace errors or conflict markers."
}

git diff --staged
& git commit -m $Message
exit $LASTEXITCODE
