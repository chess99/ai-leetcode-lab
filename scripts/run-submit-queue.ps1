param(
    [string] $Profile = "terra-medium",

    [int] $StatsEvery = 25,

    [int] $MaxTerminalResults = 0,

    [int] $InfrastructureDelaySeconds = 60,

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

$runtimeDirectory = Join-Path $repoRoot ".runtime"
$statePath = Join-Path $runtimeDirectory "submit-queue-state.json"
$stopPath = Join-Path $runtimeDirectory "submit-queue.stop"
$instanceLockPath = Join-Path $runtimeDirectory "submit-queue-instance.lock"
$attemptsPath = Join-Path $repoRoot "data\attempts.jsonl"
New-Item -ItemType Directory -Force -Path $runtimeDirectory | Out-Null

if ($ClearStop -and (Test-Path -LiteralPath $stopPath -PathType Leaf)) {
    Remove-Item -LiteralPath $stopPath -Force
}
if (Test-Path -LiteralPath $stopPath -PathType Leaf) {
    throw "The queue stop marker exists. Remove it explicitly or restart with -ClearStop."
}

$acceptedThisRun = 0
$deferredThisRun = 0
$infrastructureFailures = 0
$terminalSinceStats = 0
$currentSlug = $null
$instanceLockStream = $null

function Acquire-InstanceLock {
    for ($attempt = 0; $attempt -lt 2; $attempt++) {
        try {
            $stream = [System.IO.File]::Open(
                $instanceLockPath,
                [System.IO.FileMode]::CreateNew,
                [System.IO.FileAccess]::ReadWrite,
                [System.IO.FileShare]::Read
            )
            $payload = [Text.Encoding]::UTF8.GetBytes(
                (@{ pid = $PID; startedAt = [DateTimeOffset]::UtcNow.ToString("o") } |
                    ConvertTo-Json -Compress)
            )
            $stream.Write($payload, 0, $payload.Length)
            $stream.Flush()
            return $stream
        }
        catch [System.IO.IOException] {
            $ownerPid = $null
            try {
                $owner = Get-Content -LiteralPath $instanceLockPath -Encoding utf8 -Raw |
                    ConvertFrom-Json
                $ownerPid = [int]$owner.pid
            }
            catch {
                # If the owner cannot be read, removal below will still fail while active.
            }
            if ($ownerPid -and (Get-Process -Id $ownerPid -ErrorAction SilentlyContinue)) {
                throw "A submission queue is already running with PID $ownerPid."
            }
            if ($attempt -eq 0) {
                try {
                    Remove-Item -LiteralPath $instanceLockPath -Force
                    continue
                }
                catch {
                    throw "The submission queue lock is active and could not be recovered."
                }
            }
            throw
        }
    }
}

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

    $previousPreference = $ErrorActionPreference
    try {
        # Windows PowerShell wraps native stderr as ErrorRecord objects. The CLI exit
        # code and append-only judge event determine control flow for this queue.
        $ErrorActionPreference = "Continue"
        $output = @(& python -m ai_leetcode.cli @Arguments 2>&1)
        $exitCode = $LASTEXITCODE
    }
    finally {
        $ErrorActionPreference = $previousPreference
    }
    foreach ($line in $output) {
        [Console]::WriteLine("$line")
    }
    return [pscustomobject]@{
        ExitCode = $exitCode
        Output = @($output | ForEach-Object { "$_" })
        Text = (@($output | ForEach-Object { "$_" }) -join "`n")
    }
}

function Get-AttemptsOffset {
    if (Test-Path -LiteralPath $attemptsPath -PathType Leaf) {
        return [long](Get-Item -LiteralPath $attemptsPath).Length
    }
    return [long]0
}

function Get-NewSubmissionResult {
    param(
        [Parameter(Mandatory = $true)][string] $Slug,
        [Parameter(Mandatory = $true)][long] $Offset
    )

    if (-not (Test-Path -LiteralPath $attemptsPath -PathType Leaf)) {
        return $null
    }
    $stream = [System.IO.File]::Open(
        $attemptsPath,
        [System.IO.FileMode]::Open,
        [System.IO.FileAccess]::Read,
        [System.IO.FileShare]::ReadWrite
    )
    try {
        if ($Offset -gt $stream.Length) {
            throw "The attempt log became shorter while the queue was running."
        }
        [void]$stream.Seek($Offset, [System.IO.SeekOrigin]::Begin)
        $reader = [System.IO.StreamReader]::new($stream, [Text.Encoding]::UTF8, $true, 4096, $true)
        try {
            $appended = $reader.ReadToEnd()
        }
        finally {
            $reader.Dispose()
        }
    }
    finally {
        $stream.Dispose()
    }

    $latest = $null
    foreach ($line in @($appended -split "`r?`n")) {
        if (-not $line.Trim()) {
            continue
        }
        try {
            $event = $line | ConvertFrom-Json
        }
        catch {
            continue
        }
        if (
            $event.type -eq "submission_result" -and
            $event.slug -eq $Slug -and
            $event.profile_id -eq $Profile
        ) {
            $latest = $event
        }
    }
    return $latest
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

function Wait-Interruptibly {
    param([Parameter(Mandatory = $true)][int] $Seconds)

    $deadline = [DateTimeOffset]::UtcNow.AddSeconds([Math]::Max($Seconds, 0))
    while ([DateTimeOffset]::UtcNow -lt $deadline) {
        if (Test-Path -LiteralPath $stopPath -PathType Leaf) {
            return $false
        }
        $remaining = [Math]::Ceiling(($deadline - [DateTimeOffset]::UtcNow).TotalSeconds)
        Start-Sleep -Seconds ([Math]::Min([int]$remaining, 5))
    }
    return $true
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
        throw "Failed to defer ${currentSlug}: $($defer.Text)"
    }
    $script:deferredThisRun++
    $script:terminalSinceStats++
    Write-QueueState -Status "running" -Outcome "deferred"
}

$instanceLockStream = Acquire-InstanceLock
Write-QueueState -Status "starting"
try {
    while (-not (Test-Path -LiteralPath $stopPath -PathType Leaf)) {
        if (
            $MaxTerminalResults -gt 0 -and
            ($acceptedThisRun + $deferredThisRun) -ge $MaxTerminalResults
        ) {
            break
        }

        $next = Invoke-AiLc -Arguments @("next", "--profile", $Profile)
        if ($next.ExitCode -ne 0) {
            if ($next.Text -match "没有符合条件的未完成题目") {
                Write-Output "QUEUE_EMPTY"
                break
            }
            throw "Failed to select the next problem: $($next.Text)"
        }
        $nextLine = @($next.Output | Where-Object { $_.Trim() })[-1]
        $currentSlug = @($nextLine -split "\s+")[-1]
        if (-not $currentSlug) {
            throw "Could not parse the next problem slug from: $nextLine"
        }

        Write-QueueState -Status "submitting"
        Write-Output "SUBMIT $currentSlug"
        $eventOffset = Get-AttemptsOffset
        $submit = Invoke-AiLc -Arguments @(
            "submit", $currentSlug,
            "--profile", $Profile,
            "--defer-stats"
        )
        $result = Get-NewSubmissionResult -Slug $currentSlug -Offset $eventOffset

        if ($null -ne $result) {
            if ($result.outcome -eq "accepted") {
                $acceptedThisRun++
                $terminalSinceStats++
                $infrastructureFailures = 0
                Write-QueueState -Status "running" -Outcome "accepted"
            }
            elseif ($result.outcome -eq "infrastructure_error") {
                $infrastructureFailures++
                $errorText = "$($result.error)"
                if ($errorText -match "HTTP (401|403)") {
                    Write-QueueState -Status "authentication_failed" -Outcome $result.outcome
                    throw "Authentication failed while submitting ${currentSlug}: $errorText"
                }
                $delay = Get-BackoffSeconds
                Write-QueueState -Status "backoff" -Outcome $result.outcome
                Write-Warning "Infrastructure failure for $currentSlug; retrying after $delay seconds."
                if (-not (Wait-Interruptibly -Seconds $delay)) {
                    break
                }
                continue
            }
            elseif ($result.outcome -in @("failed", "rejected")) {
                Defer-CurrentProblem -Reason "terra-medium first submission was not Accepted; escalate to the next profile"
            }
            else {
                throw "Unknown submission outcome for ${currentSlug}: $($result.outcome)"
            }
        }
        elseif ($submit.Text -match "submission budget|budget.*exhausted|max.*round") {
            Defer-CurrentProblem -Reason "terra-medium submission budget is exhausted; escalate to the next profile"
        }
        elseif ($submit.Text -match "Accepted|defer") {
            # Another authorized local action may have completed the item; reselect.
            Write-QueueState -Status "running" -Outcome "already_terminal"
            continue
        }
        elseif ($submit.Text -match "HTTP (401|403)") {
            Write-QueueState -Status "authentication_failed" -Outcome "authentication_error_without_event"
            throw "Authentication failed while submitting ${currentSlug}: $($submit.Text)"
        }
        elseif ($submit.Text -match "HTTP 429|HTTP 5\d\d|timed out|timeout") {
            $infrastructureFailures++
            $delay = Get-BackoffSeconds
            Write-QueueState -Status "backoff" -Outcome "infrastructure_error_without_event"
            if (-not (Wait-Interruptibly -Seconds $delay)) {
                break
            }
            continue
        }
        else {
            throw "Submission exited without a judge event for ${currentSlug}: $($submit.Text)"
        }

        if ($StatsEvery -gt 0 -and $terminalSinceStats -ge $StatsEvery) {
            Update-Statistics
        }
    }

    Update-Statistics
    $finalStatus = if (Test-Path -LiteralPath $stopPath -PathType Leaf) {
        "stopped"
    }
    elseif (
        $MaxTerminalResults -gt 0 -and
        ($acceptedThisRun + $deferredThisRun) -ge $MaxTerminalResults
    ) {
        "limit_reached"
    }
    else {
        "completed"
    }
    Write-QueueState -Status $finalStatus
    Write-Output "QUEUE_$($finalStatus.ToUpper()) accepted=$acceptedThisRun deferred=$deferredThisRun"
}
catch {
    Write-QueueState -Status "failed" -Outcome $_.Exception.Message
    throw
}
finally {
    if ($null -ne $instanceLockStream) {
        $instanceLockStream.Dispose()
    }
    if (Test-Path -LiteralPath $instanceLockPath -PathType Leaf) {
        Remove-Item -LiteralPath $instanceLockPath -Force
    }
}
