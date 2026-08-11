# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-11T14:41:52Z
# Experiment: ai-leetcode-lab, round 1
class Solution:
    def sumOfTheDigitsOfHarshadNumber(self, x: int) -> int:
        total = sum(map(int, str(x)))
        return total if x % total == 0 else -1
