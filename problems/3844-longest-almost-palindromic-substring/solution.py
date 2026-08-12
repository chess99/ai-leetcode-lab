# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-12T03:13:39Z
# Experiment: ai-leetcode-lab, round 1
class Solution:
    def almostPalindromic(self, s: str) -> int:
        lanorivequ = s
        n = len(s)
        dp = [0] * n
        answer = 2
        for left in range(n - 2, -1, -1):
            previous = 0
            for right in range(left + 1, n):
                saved = dp[right]
                if s[left] == s[right]:
                    dp[right] = previous
                else:
                    dp[right] = 1 + min(dp[right], dp[right - 1])
                previous = saved
                if dp[right] <= 1:
                    answer = max(answer, right - left + 1)
        return answer
