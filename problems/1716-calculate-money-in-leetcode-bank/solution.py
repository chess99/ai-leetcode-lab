# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-11T12:26:05Z
# Experiment: ai-leetcode-lab, round 1
class Solution:
    def totalMoney(self, n: int) -> int:
        weeks, days = divmod(n, 7)
        return 28 * weeks + 7 * weeks * (weeks - 1) // 2 + days * (weeks + 1) + days * (days - 1) // 2
