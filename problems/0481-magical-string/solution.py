# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-11T17:10:25Z
# Experiment: ai-leetcode-lab, round 1
class Solution:
    def magicalString(self, n: int) -> int:
        if n <= 0:
            return 0
        if n <= 3:
            return 1

        sequence = [1, 2, 2]
        read = 2
        next_value = 1
        ones = 1
        while len(sequence) < n:
            repeat = sequence[read]
            sequence.extend([next_value] * repeat)
            if next_value == 1:
                ones += min(repeat, n - (len(sequence) - repeat))
            next_value = 3 - next_value
            read += 1
        return ones
