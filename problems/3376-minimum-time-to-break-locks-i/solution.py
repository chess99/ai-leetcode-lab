# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-11T21:59:16Z
# Experiment: ai-leetcode-lab, round 1
from typing import List


class Solution:
    def findMinimumTime(self, strength: List[int], k: int) -> int:
        n = len(strength)
        dp = [float('inf')] * (1 << n)
        dp[0] = 0
        for mask in range(1 << n):
            power = 1 + mask.bit_count() * k
            for lock in range(n):
                if not mask >> lock & 1:
                    nxt = mask | (1 << lock)
                    dp[nxt] = min(dp[nxt], dp[mask] + (strength[lock] + power - 1) // power)
        return dp[-1]
