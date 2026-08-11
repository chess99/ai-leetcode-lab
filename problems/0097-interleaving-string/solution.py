# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-11T16:18:30Z
# Experiment: ai-leetcode-lab, round 1
class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        if len(s1) + len(s2) != len(s3):
            return False

        dp = [False] * (len(s2) + 1)
        dp[0] = True
        for column in range(1, len(s2) + 1):
            dp[column] = dp[column - 1] and s2[column - 1] == s3[column - 1]

        for row in range(1, len(s1) + 1):
            dp[0] = dp[0] and s1[row - 1] == s3[row - 1]
            for column in range(1, len(s2) + 1):
                index = row + column - 1
                dp[column] = (dp[column] and s1[row - 1] == s3[index]) or (
                    dp[column - 1] and s2[column - 1] == s3[index]
                )
        return dp[-1]
