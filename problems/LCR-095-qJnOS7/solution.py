# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-12T04:46:22Z
# Experiment: ai-leetcode-lab, round 1
class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        if len(text1) < len(text2):
            text1, text2 = text2, text1
        dp = [0] * (len(text2) + 1)
        for char1 in text1:
            diagonal = 0
            for index, char2 in enumerate(text2, 1):
                above = dp[index]
                if char1 == char2:
                    dp[index] = diagonal + 1
                else:
                    dp[index] = max(dp[index], dp[index - 1])
                diagonal = above
        return dp[-1]
