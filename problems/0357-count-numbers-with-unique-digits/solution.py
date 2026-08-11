# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-11T16:47:59Z
# Experiment: ai-leetcode-lab, round 1
class Solution:
    def countNumbersWithUniqueDigits(self, n: int) -> int:
        total, current, choices = 1, 9, 9
        for _ in range(min(n, 10)):
            total += current
            current *= choices
            choices -= 1
        return total
