# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-sol
# Reasoning effort: medium
# Profile: sol-medium
# Original candidate: Codex Desktop / gpt-5.6-terra / medium / terra-medium
class Solution:
    def minimumSubstringsInPartition(self, s: str) -> int:
        n = len(s)
        # dp[i] 表示前缀 s[:i] 的最少平衡子串数。
        dp = [0] + [n] * n

        for left in range(n):
            count = [0] * 26
            distinct = 0
            max_frequency = 0

            for right in range(left, n):
                index = ord(s[right]) - ord("a")
                if count[index] == 0:
                    distinct += 1
                count[index] += 1
                if count[index] > max_frequency:
                    max_frequency = count[index]

                length = right - left + 1
                if length == distinct * max_frequency:
                    candidate = dp[left] + 1
                    if candidate < dp[right + 1]:
                        dp[right + 1] = candidate

        return dp[n]
