# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-12T05:00:56Z
# Experiment: ai-leetcode-lab, round 1
class Solution:
    def waysToChange(self, n: int) -> int:
        modulus = 1_000_000_007
        dp = [0] * (n + 1)
        dp[0] = 1
        for coin in (1, 5, 10, 25):
            for amount in range(coin, n + 1):
                dp[amount] = (dp[amount] + dp[amount - coin]) % modulus
        return dp[n]
