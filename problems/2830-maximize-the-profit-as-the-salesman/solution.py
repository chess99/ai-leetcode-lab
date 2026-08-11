# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-11T21:23:06Z
# Experiment: ai-leetcode-lab, round 1
from typing import List
class Solution:
    def maximizeTheProfit(self, n: int, offers: List[List[int]]) -> int:
        ending = [[] for _ in range(n)]
        for start, end, gold in offers: ending[end].append((start, gold))
        dp = [0] * (n + 1)
        for i in range(n):
            dp[i + 1] = dp[i]
            for start, gold in ending[i]: dp[i + 1] = max(dp[i + 1], dp[start] + gold)
        return dp[n]
