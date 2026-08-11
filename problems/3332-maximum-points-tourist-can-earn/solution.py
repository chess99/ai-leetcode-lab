# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-11T21:59:15Z
# Experiment: ai-leetcode-lab, round 1
from typing import List


class Solution:
    def maxScore(self, n: int, k: int, stayScore: List[List[int]], travelScore: List[List[int]]) -> int:
        dp = [0] * n
        for day in range(k):
            nxt = [0] * n
            for dest in range(n):
                best = dp[dest] + stayScore[day][dest]
                for src in range(n):
                    best = max(best, dp[src] + travelScore[src][dest])
                nxt[dest] = best
            dp = nxt
        return max(dp)
