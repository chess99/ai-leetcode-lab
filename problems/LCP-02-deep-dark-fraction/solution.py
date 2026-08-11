# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-11T15:26:45Z
# Experiment: ai-leetcode-lab, round 1
class Solution:
    def fraction(self, cont: List[int]) -> List[int]:
        numerator, denominator = cont[-1], 1
        for value in reversed(cont[:-1]):
            numerator, denominator = value * numerator + denominator, numerator
        return [numerator, denominator]
