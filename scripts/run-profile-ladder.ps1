param(
    [string[]] $Profiles = @(),

    [int] $StatsEvery = 25,

    [switch] $ClearStop
)

$ErrorActionPreference = "Stop"
$repoRoot = (git rev-parse --show-toplevel 2>$null).Trim()
if (-not $repoRoot) {
    throw "The current directory is not inside a Git repository."
}
Set-Location -LiteralPath $repoRoot
$env:PYTHONUTF8 = "1"
$env:PYTHONPATH = $repoRoot

if ($Profiles.Count -eq 0) {
    $profileOutput = @(& python -m ai_leetcode.cli profiles 2>&1)
    if ($LASTEXITCODE -ne 0) {
        throw "Failed to read the configured execution ladder: $($profileOutput -join ' ')"
    }
    $profileConfig = ($profileOutput -join "`n") | ConvertFrom-Json
    $Profiles = @($profileConfig.executionLadder)
    if ($Profiles.Count -eq 0) {
        throw "config/profiles.json does not define executionLadder."
    }
}

$runtimeDirectory = Join-Path $repoRoot ".runtime"
$statePath = Join-Path $runtimeDirectory "profile-ladder-state.json"
$stopPath = Join-Path $runtimeDirectory "profile-ladder.stop"
$queueStopPath = Join-Path $runtimeDirectory "submit-queue.stop"
$queueScript = Join-Path $repoRoot "scripts\run-submit-queue.ps1"
New-Item -ItemType Directory -Force -Path $runtimeDirectory | Out-Null

if ($ClearStop) {
    foreach ($path in @($stopPath, $queueStopPath)) {
        if (Test-Path -LiteralPath $path -PathType Leaf) {
            Remove-Item -LiteralPath $path -Force
        }
    }
}
if (Test-Path -LiteralPath $stopPath -PathType Leaf) {
    throw "The profile ladder stop marker exists. Restart with -ClearStop."
}

function Write-LadderState {
    param(
        [Parameter(Mandatory = $true)][string] $Status,
        [string] $Profile = "",
        [int] $ExitCode = 0
    )
    [ordered]@{
        schemaVersion = 1
        pid = $PID
        status = $Status
        currentProfile = $Profile
        profiles = $Profiles
        lastExitCode = $ExitCode
        updatedAt = [DateTimeOffset]::UtcNow.ToString("o")
    } | ConvertTo-Json | Set-Content -LiteralPath $statePath -Encoding utf8
}

Write-LadderState -Status "starting"
foreach ($profile in $Profiles) {
    if (Test-Path -LiteralPath $stopPath -PathType Leaf) {
        Write-LadderState -Status "stopped" -Profile $profile
        exit 0
    }
    Write-LadderState -Status "running" -Profile $profile
    & $queueScript -Profile $profile -StatsEvery $StatsEvery -ClearStop:$ClearStop
    $exitCode = $LASTEXITCODE
    if ($exitCode -ne 0) {
        Write-LadderState -Status "failed" -Profile $profile -ExitCode $exitCode
        exit $exitCode
    }
    $ClearStop = $false
}

Write-LadderState -Status "completed"
Write-Output "PROFILE_LADDER_COMPLETED"
