param(
    [Parameter(ValueFromRemainingArguments = $true)]
    [string[]] $Arguments
)

$ErrorActionPreference = "Stop"
$env:PYTHONUTF8 = "1"
python -m ai_leetcode.cli @Arguments
exit $LASTEXITCODE
