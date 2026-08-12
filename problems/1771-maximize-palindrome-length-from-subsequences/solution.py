# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-12T11:06:43Z
# Experiment: ai-leetcode-lab, round 1
class Solution:
    def longestPalindrome(self, word1: str, word2: str) -> int:
        text = word1 + word2
        size = len(text)
        boundary = len(word1)
        dp = [[0] * size for _ in range(size)]
        answer = 0
        for left in range(size - 1, -1, -1):
            dp[left][left] = 1
            for right in range(left + 1, size):
                if text[left] == text[right]:
                    dp[left][right] = 2 + (dp[left + 1][right - 1]
                                           if left + 1 < right else 0)
                    if left < boundary <= right:
                        answer = max(answer, dp[left][right])
                else:
                    dp[left][right] = max(dp[left + 1][right],
                                          dp[left][right - 1])
        return answer
