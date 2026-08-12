# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-12T11:06:49Z
# Experiment: ai-leetcode-lab, round 1
class Solution:
    def rearrangeSticks(self, n: int, k: int) -> int:
        modulus = 1_000_000_007
        dp = [0] * (k + 1)
        dp[0] = 1
        for sticks in range(1, n + 1):
            following = [0] * (k + 1)
            for visible in range(1, min(sticks, k) + 1):
                following[visible] = (
                    dp[visible - 1] + (sticks - 1) * dp[visible]) % modulus
            dp = following
        return dp[k]
