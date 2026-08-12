# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-12T08:09:54Z
# Experiment: ai-leetcode-lab, round 1
class Solution:
    def numberOfArrays(self, s: str, k: int) -> int:
        modulus = 1_000_000_007
        size = len(s)
        dp = [0] * (size + 1)
        dp[size] = 1
        maximum_length = len(str(k))
        for index in range(size - 1, -1, -1):
            if s[index] == '0':
                continue
            value = 0
            for end in range(index, min(size, index + maximum_length)):
                value = value * 10 + int(s[end])
                if value > k:
                    break
                dp[index] += dp[end + 1]
            dp[index] %= modulus
        return dp[0]
