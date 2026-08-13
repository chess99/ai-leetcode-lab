param(
    [string] $Profile = "terra-medium",

    [int] $StatsEvery = 25,

    [int] $MaxTerminalResults = 0,

    [int] $InfrastructureDelaySeconds = 60
)

$ErrorActionPreference = "Stop"
$repoRoot = (git rev-parse --show-toplevel 2>$null).Trim()
if (-not $repoRoot) {
    throw "The current directory is not inside a Git repository."
}
Set-Location -LiteralPath $repoRoot
$env:PYTHONUTF8 = "1"
$env:PYTHONPATH = $repoRoot

$runtimeDirectory = Join-Path $repoRoot ".runtime"
$statePath = Join-Path $runtimeDirectory "submit-queue-state.json"
$stopPath = Join-Path $runtimeDirectory "submit-queue.stop"
$attemptsPath = Join-Path $repoRoot "data\attempts.jsonl"
New-Item -ItemType Directory -Force -Path $runtimeDirectory | Out-Null

if (Test-Path -LiteralPath $stopPath) {
    Remove-Item -LiteralPath $stopPath -Force
}

$acceptedThisRun = 0
$deferredThisRun = 0
$infrastructureFailures = 0
$terminalSinceStats = 0
$currentSlug = $null

function Write-QueueState {
    param(
        [Parameter(Mandatory = $true)]
        [string] $Status,

        [string] $Outcome = ""
    )

    $state = [ordered]@{
        schemaVersion = 1
        pid = $PID
        profile = $Profile
        status = $Status
        currentSlug = $currentSlug
        lastOutcome = $Outcome
        acceptedThisRun = $acceptedThisRun
        deferredThisRun = $deferredThisRun
        infrastructureFailures = $infrastructureFailures
        updatedAt = [DateTimeOffset]::UtcNow.ToString("o")
    }
    $state | ConvertTo-Json | Set-Content -LiteralPath $statePath -Encoding utf8
}

function Invoke-AiLc {
    param([Parameter(Mandatory = $true)][string[]] $Arguments)

    $output = @(& python -m ai_leetcode.cli @Arguments 2>&1)
    $exitCode = $LASTEXITCODE
    foreach ($line in $output) {
        [Console]::WriteLine("$line")
    }
    return [pscustomobject]@{
        ExitCode = $exitCode
        Output = $output
    }
}

function Get-LatestSubmissionResult {
    param([Parameter(Mandatory = $true)][string] $Slug)

    if (-not (Test-Path -LiteralPath $attemptsPath -PathType Leaf)) {
        return $null
    }
    $lines = @(Get-Content -LiteralPath $attemptsPath -Encoding utf8)
    for ($index = $lines.Count - 1; $index -ge 0; $index--) {
        if (-not $lines[$index].Trim()) {
            continue
        }
        try {
            $event = $lines[$index] | ConvertFrom-Json
        }
        catch {
            continue
        }
        if (
            $event.type -eq "submission_result" -and
            $event.slug -eq $Slug -and
            $event.profile_id -eq $Profile
        ) {
            return $event
        }
    }
    return $null
}

function Get-BackoffSeconds {
    $backoffPath = Join-Path $runtimeDirectory "remote-backoff.json"
    if (-not (Test-Path -LiteralPath $backoffPath -PathType Leaf)) {
        return $InfrastructureDelaySeconds
    }
    try {
        $backoff = Get-Content -LiteralPath $backoffPath -Encoding utf8 -Raw | ConvertFrom-Json
        $remaining = [Math]::Ceiling(
            [double]$backoff.untilUnix - [DateTimeOffset]::UtcNow.ToUnixTimeSeconds()
        )
        return [Math]::Max([int]$remaining, 1)
    }
    catch {
        return $InfrastructureDelaySeconds
    }
}

function Update-Statistics {
    Write-QueueState -Status "updating_stats"
    $stats = Invoke-AiLc -Arguments @("stats")
    if ($stats.ExitCode -ne 0) {
        throw "Failed to rebuild statistics."
    }
    $script:terminalSinceStats = 0
}

function Defer-CurrentProblem {
    param([Parameter(Mandatory = $true)][string] $Reason)

    $defer = Invoke-AiLc -Arguments @(
        "defer", $currentSlug,
        "--profile", $Profile,
        "--reason", $Reason
    )
    if ($defer.ExitCode -ne 0) {
        throw "Failed to defer $currentSlug."
    }
    $script:deferredThisRun++
    $script:terminalSinceStats++
    Write-QueueState -Status "running" -Outcome "deferred"
}

Write-QueueState -Status "starting"
try {
    while (-not (Test-Path -LiteralPath $stopPath)) {
        if (
            $MaxTerminalResults -gt 0 -and
            ($acceptedThisRun + $deferredThisRun) -ge $MaxTerminalResults
        ) {
            break
        }

        $next = Invoke-AiLc -Arguments @("next", "--profile", $Profile)
        if ($next.ExitCode -ne 0) {
            Write-Output "QUEUE_EMPTY"
            break
        }
        $nextLine = @($next.Output | ForEach-Object { "$_" } | Where-Object { $_.Trim() })[-1]
        $currentSlug = @($nextLine -split "\s+")[-1]
        if (-not $currentSlug) {
            throw "Could not parse the next problem slug from: $nextLine"
        }

        Write-QueueState -Status "submitting"
        Write-Output "SUBMIT $currentSlug"
        $previous = Get-LatestSubmissionResult -Slug $currentSlug
        $submit = Invoke-AiLc -Arguments @(
            "submit", $currentSlug,
            "--profile", $Profile,
            "--defer-stats"
        )
        $result = Get-LatestSubmissionResult -Slug $currentSlug

        if ($submit.ExitCode -eq 0 -and $result.outcome -eq "accepted") {
            $acceptedThisRun++
            $terminalSinceStats++
            $infrastructureFailures = 0
            Write-QueueState -Status "running" -Outcome "accepted"
        }
        elseif ($null -ne $result -and $result.event_id -ne $previous.event_id) {
            if ($result.outcome -eq "infrastructure_error") {
                $infrastructureFailures++
                $errorText = "$($result.error)"
                if ($errorText -match "HTTP (401|403)|认证|登录") {
                    Write-QueueState -Status "authentication_failed" -Outcome $result.outcome
                    throw "Authentication failed while submitting ${currentSlug}: $errorText"
                }
                $delay = Get-BackoffSeconds
                Write-QueueState -Status "backoff" -Outcome $result.outcome
                Write-Warning "Infrastructure failure for $currentSlug; retrying after $delay seconds."
                Start-Sleep -Seconds $delay
                continue
            }

            Defer-CurrentProblem -Reason "terra-medium 第一次正式提交未 Accepted，保留给更高档位按实验阶梯重试"
        }
        else {
            # No new judge result normally means the Profile budget was already exhausted.
            Defer-CurrentProblem -Reason "terra-medium 已无可用正式提交预算，保留给更高档位按实验阶梯重试"
        }

        if ($StatsEvery -gt 0 -and $terminalSinceStats -ge $StatsEvery) {
            Update-Statistics
        }
    }

    Update-Statistics
    $finalStatus = if (Test-Path -LiteralPath $stopPath) { "stopped" } else { "completed" }
    Write-QueueState -Status $finalStatus
    Write-Output "QUEUE_$($finalStatus.ToUpper()) accepted=$acceptedThisRun deferred=$deferredThisRun"
}
catch {
    Write-QueueState -Status "failed" -Outcome $_.Exception.Message
    throw
}
