# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-12T05:24:55Z
# Experiment: ai-leetcode-lab, round 1
class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        if len(t) > len(s):
            return 0
        dp = [0] * (len(t) + 1)
        dp[0] = 1
        for source_char in s:
            for index in range(len(t), 0, -1):
                if source_char == t[index - 1]:
                    dp[index] += dp[index - 1]
        return dp[-1]
