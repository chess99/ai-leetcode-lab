# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-11T15:16:00Z
# Experiment: ai-leetcode-lab, round 1
class Solution:
    def minimumFlips(self, n: int) -> int:
        bits = bin(n)[2:]
        return sum(left != right for left, right in zip(bits, reversed(bits)))
