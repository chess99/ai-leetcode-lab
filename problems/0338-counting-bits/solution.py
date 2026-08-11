# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-11T10:29:10Z
# Experiment: ai-leetcode-lab, round 1
class Solution:
    def countBits(self, n: int) -> List[int]:
        bits = [0] * (n + 1)
        for value in range(1, n + 1):
            bits[value] = bits[value >> 1] + (value & 1)
        return bits
