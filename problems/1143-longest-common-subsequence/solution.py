# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-11T18:24:05Z
# Experiment: ai-leetcode-lab, round 1
class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        if len(text1) < len(text2):
            text1, text2 = text2, text1
        dp = [0] * (len(text2) + 1)
        for first in text1:
            previous = 0
            for index, second in enumerate(text2, 1):
                saved = dp[index]
                if first == second:
                    dp[index] = previous + 1
                else:
                    dp[index] = max(dp[index], dp[index - 1])
                previous = saved
        return dp[-1]
