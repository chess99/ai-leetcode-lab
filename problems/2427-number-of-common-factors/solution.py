# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-11T14:03:12Z
# Experiment: ai-leetcode-lab, round 1
class Solution:
    def commonFactors(self, a: int, b: int) -> int:
        return sum(a % value == 0 and b % value == 0 for value in range(1, min(a, b) + 1))
