# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-11T21:46:17Z
# Experiment: ai-leetcode-lab, round 1
from typing import List

class Solution:
    def maxRemovals(self, source: str, pattern: str, targetIndices: List[int]) -> int:
        removable = set(targetIndices)
        impossible = -10**9
        dp = [impossible] * (len(pattern) + 1)
        dp[0] = 0
        for index, char in enumerate(source):
            next_dp = dp[:]
            for matched in range(len(pattern) - 1, -1, -1):
                if dp[matched] != impossible and char == pattern[matched]:
                    next_dp[matched + 1] = max(next_dp[matched + 1], dp[matched])
            if index in removable:
                for matched in range(len(pattern) + 1):
                    if dp[matched] != impossible:
                        next_dp[matched] = max(next_dp[matched], dp[matched] + 1)
            dp = next_dp
        return dp[-1]
