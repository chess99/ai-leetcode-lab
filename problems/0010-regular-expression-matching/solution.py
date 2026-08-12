# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-12T05:24:51Z
# Experiment: ai-leetcode-lab, round 1
class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        rows, cols = len(s), len(p)
        dp = [[False] * (cols + 1) for _ in range(rows + 1)]
        dp[0][0] = True
        for j in range(2, cols + 1):
            if p[j - 1] == "*":
                dp[0][j] = dp[0][j - 2]
        for i in range(1, rows + 1):
            for j in range(1, cols + 1):
                if p[j - 1] == "*":
                    dp[i][j] = dp[i][j - 2]
                    if p[j - 2] in (".", s[i - 1]):
                        dp[i][j] |= dp[i - 1][j]
                elif p[j - 1] in (".", s[i - 1]):
                    dp[i][j] = dp[i - 1][j - 1]
        return dp[rows][cols]
