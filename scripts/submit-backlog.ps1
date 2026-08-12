param(
    [Parameter(Mandatory = $true)]
    [string] $InputFile,

    [string] $Profile = "terra-medium",

    [int] $Limit = 0
)

$ErrorActionPreference = "Continue"
$repoRoot = (git rev-parse --show-toplevel 2>$null).Trim()
if (-not $repoRoot) {
    throw "The current directory is not inside a Git repository."
}
Set-Location -LiteralPath $repoRoot
$env:PYTHONUTF8 = "1"

if (-not (Test-Path -LiteralPath $InputFile -PathType Leaf)) {
    throw "Input file does not exist: $InputFile"
}

$selectors = @(
    Get-Content -LiteralPath $InputFile -Encoding utf8 |
        ForEach-Object { $_.Trim() } |
        Where-Object { $_ -and -not $_.StartsWith("#") }
)
if ($Limit -gt 0) {
    $selectors = @($selectors | Select-Object -First $Limit)
}

$completed = 0
foreach ($selector in $selectors) {
    Write-Output "SUBMIT $selector"
    python -m ai_leetcode.cli submit $selector --profile $Profile --defer-stats
    $exitCode = $LASTEXITCODE
    if ($exitCode -eq 0) {
        $completed++
        continue
    }

    if (Test-Path -LiteralPath ".runtime/remote-backoff.json") {
        Write-Warning "LeetCode registered a remote backoff; stopping this batch immediately."
        break
    }

    Write-Warning "Submission did not pass for $selector (exit $exitCode); continuing with the next problem."
}

python -m ai_leetcode.cli stats
if ($LASTEXITCODE -ne 0) {
    throw "Failed to rebuild statistics after the submission batch."
}
Write-Output "BATCH_COMPLETED $completed/$($selectors.Count)"
