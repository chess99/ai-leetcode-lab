# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-12T04:46:23Z
# Experiment: ai-leetcode-lab, round 1
class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        dp = [1] * n
        for _ in range(1, m):
            for column in range(1, n):
                dp[column] += dp[column - 1]
        return dp[-1]
