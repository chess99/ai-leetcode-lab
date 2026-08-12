# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-12T08:09:54Z
# Experiment: ai-leetcode-lab, round 1
class Solution:
    def numOfArrays(self, n: int, m: int, k: int) -> int:
        modulus = 1_000_000_007
        dp = [[0] * (m + 1) for _ in range(k + 1)]
        for maximum in range(1, m + 1):
            dp[1][maximum] = 1
        for _ in range(1, n):
            following = [[0] * (m + 1) for _ in range(k + 1)]
            for cost in range(1, k + 1):
                prefix = 0
                for maximum in range(1, m + 1):
                    if cost > 1:
                        prefix += dp[cost - 1][maximum - 1]
                    following[cost][maximum] = (
                        dp[cost][maximum] * maximum + prefix) % modulus
            dp = following
        return sum(dp[k]) % modulus
