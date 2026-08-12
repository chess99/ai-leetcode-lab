# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-12T08:09:58Z
# Experiment: ai-leetcode-lab, round 1
class Solution:
    def winnerSquareGame(self, n: int) -> bool:
        dp = [False] * (n + 1)
        for value in range(1, n + 1):
            dp[value] = any(not dp[value - root * root] for root in range(1, int(value ** .5) + 1))
        return dp[n]
