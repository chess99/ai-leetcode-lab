# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-11T19:48:05Z
# Experiment: ai-leetcode-lab, round 1
class Solution:
    def countGoodNumbers(self, n: int) -> int:
        mod = 10 ** 9 + 7
        return pow(5, (n + 1) // 2, mod) * pow(4, n // 2, mod) % mod
