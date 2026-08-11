# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-11T17:13:09Z
# Experiment: ai-leetcode-lab, round 1
class Solution:
    def longestPalindromeSubseq(self, s: str) -> int:
        if not s:
            return 0

        length = len(s)
        dp = [0] * length

        for left in range(length - 1, -1, -1):
            dp[left] = 1
            diagonal = 0
            for right in range(left + 1, length):
                previous = dp[right]
                if s[left] == s[right]:
                    dp[right] = diagonal + 2
                else:
                    dp[right] = max(dp[right], dp[right - 1])
                diagonal = previous

        return dp[-1]
