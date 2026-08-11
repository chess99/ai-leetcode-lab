# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-11T20:37:16Z
# Experiment: ai-leetcode-lab, round 1
class Solution:
    def minimizeXor(self, num1: int, num2: int) -> int:
        bits_needed = num2.bit_count()
        result = 0

        for bit in range(30, -1, -1):
            if bits_needed > 0 and num1 & (1 << bit):
                result |= 1 << bit
                bits_needed -= 1

        for bit in range(31):
            if bits_needed == 0:
                break
            if result & (1 << bit) == 0:
                result |= 1 << bit
                bits_needed -= 1

        return result
