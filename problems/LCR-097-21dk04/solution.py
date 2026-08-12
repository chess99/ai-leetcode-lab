# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-12T18:34:26Z
# Experiment: ai-leetcode-lab, round 1
class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        dp = [0] * (len(t) + 1)
        dp[0] = 1
        for char in s:
            for index in range(len(t) - 1, -1, -1):
                if t[index] == char:
                    dp[index + 1] += dp[index]
        return dp[-1]
