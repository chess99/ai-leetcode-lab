# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-11T12:03:48Z
# Experiment: ai-leetcode-lab, round 1
class Solution:
    def xorOperation(self, n: int, start: int) -> int:
        value = 0
        for index in range(n):
            value ^= start + 2 * index
        return value
