# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-11T18:26:22Z
# Experiment: ai-leetcode-lab, round 1
class Solution:
    def numRollsToTarget(self, n: int, k: int, target: int) -> int:
        modulo = 10 ** 9 + 7
        dp = [0] * (target + 1)
        dp[0] = 1
        for _ in range(n):
            next_dp = [0] * (target + 1)
            for total in range(1, target + 1):
                next_dp[total] = sum(dp[max(0, total - k):total]) % modulo
            dp = next_dp
        return dp[target]
