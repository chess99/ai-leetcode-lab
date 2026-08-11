# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-11T20:37:19Z
# Experiment: ai-leetcode-lab, round 1

class Solution:
    def makeIntegerBeautiful(self, n: int, target: int) -> int:
        original = n
        place = 1

        while sum(map(int, str(n))) > target:
            digit = (n // place) % 10
            n += (10 - digit) * place
            place *= 10

        return n - original
