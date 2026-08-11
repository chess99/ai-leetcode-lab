# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-11T15:16:03Z
# Experiment: ai-leetcode-lab, round 1
class Solution:
    def sumAndMultiply(self, n: int) -> int:
        digits = [digit for digit in str(n) if digit != "0"]
        value = int("".join(digits)) if digits else 0
        return value * sum(map(int, digits))
