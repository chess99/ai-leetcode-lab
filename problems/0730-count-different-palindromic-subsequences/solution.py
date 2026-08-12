# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-12T06:02:47Z
# Experiment: ai-leetcode-lab, round 1
class Solution:
    def countPalindromicSubsequences(self, s: str) -> int:
        modulus = 1_000_000_007
        size = len(s)
        next_same = [size] * size
        previous_same = [-1] * size
        last = {}
        for index, char in enumerate(s):
            previous_same[index] = last.get(char, -1)
            last[char] = index
        last.clear()
        for index in range(size - 1, -1, -1):
            next_same[index] = last.get(s[index], size)
            last[s[index]] = index
        dp = [[0] * size for _ in range(size)]
        for index in range(size):
            dp[index][index] = 1
        for length in range(2, size + 1):
            for left in range(size - length + 1):
                right = left + length - 1
                if s[left] != s[right]:
                    dp[left][right] = (dp[left + 1][right] + dp[left][right - 1]
                                       - dp[left + 1][right - 1]) % modulus
                    continue
                low, high = next_same[left], previous_same[right]
                inner = dp[left + 1][right - 1] if length > 2 else 0
                if low > high:
                    dp[left][right] = 2 * inner + 2
                elif low == high:
                    dp[left][right] = 2 * inner + 1
                else:
                    duplicate_inner = dp[low + 1][high - 1] if low + 1 <= high - 1 else 0
                    dp[left][right] = 2 * inner - duplicate_inner
                dp[left][right] %= modulus
        return dp[0][size - 1]
