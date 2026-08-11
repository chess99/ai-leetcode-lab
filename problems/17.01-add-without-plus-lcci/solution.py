# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-11T16:01:51Z
# Experiment: ai-leetcode-lab, round 1
class Solution:
    def add(self, a: int, b: int) -> int:
        mask = 0xFFFFFFFF
        while b:
            a, b = (a ^ b) & mask, ((a & b) << 1) & mask
        return a if a < 0x80000000 else a - 0x100000000
