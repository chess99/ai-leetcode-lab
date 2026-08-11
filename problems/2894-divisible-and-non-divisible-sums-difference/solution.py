# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-11T14:31:10Z
# Experiment: ai-leetcode-lab, round 1
class Solution:
    def differenceOfSums(self, n: int, m: int) -> int:
        total = n * (n + 1) // 2
        divisible = num * (n // m) * (n // m + 1) // 2
        return total - 2 * divisible
