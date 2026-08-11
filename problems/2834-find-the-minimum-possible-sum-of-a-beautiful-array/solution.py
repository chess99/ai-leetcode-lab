# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-11T21:23:06Z
# Experiment: ai-leetcode-lab, round 1
class Solution:
    def minimumPossibleSum(self, n: int, target: int) -> int:
        first=min(n,(target-1)//2); rest=n-first
        return (first*(first+1)//2 + rest*(2*target+rest-1)//2) % 1_000_000_007
