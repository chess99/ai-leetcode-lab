# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-11T16:44:08Z
# Experiment: ai-leetcode-lab, round 1
class Solution:
    def numSquares(self, n: int) -> int:
        dp = [0] + [n] * n
        for value in range(1, n + 1):
            square = 1
            while square * square <= value:
                dp[value] = min(dp[value], dp[value - square * square] + 1)
                square += 1
        return dp[n]
