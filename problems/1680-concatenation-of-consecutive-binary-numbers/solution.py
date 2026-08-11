# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-11T19:16:30Z
# Experiment: ai-leetcode-lab, round 1
class Solution:
    def concatenatedBinary(self, n: int) -> int:
        modulo = 1_000_000_007
        result = 0
        bit_length = 0

        for value in range(1, n + 1):
            if value & (value - 1) == 0:
                bit_length += 1
            result = ((result << bit_length) + value) % modulo

        return result
