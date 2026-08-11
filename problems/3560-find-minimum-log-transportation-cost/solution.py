# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-11T15:04:25Z
# Experiment: ai-leetcode-lab, round 1
class Solution:
    def minCuttingCost(self, n: int, m: int, k: int) -> int:
        return (n - k) * k if n > k else (m - k) * k if m > k else 0
