# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-11T18:21:12Z
# Experiment: ai-leetcode-lab, round 1
from typing import List


class Solution:
    def sampleStats(self, count: List[int]) -> List[float]:
        total = sum(count)
        weighted_sum = sum(value * frequency for value, frequency in enumerate(count))
        minimum = next(value for value, frequency in enumerate(count) if frequency)
        maximum = next(value for value in range(255, -1, -1) if count[value])
        mode = max(range(256), key=lambda value: count[value])

        left_rank = (total + 1) // 2
        right_rank = (total + 2) // 2
        seen = 0
        left_value = right_value = None
        for value, frequency in enumerate(count):
            seen += frequency
            if seen >= left_rank and left_value is None:
                left_value = value
            if seen >= right_rank:
                right_value = value
                break

        return [float(minimum), float(maximum), weighted_sum / total,
                (left_value + right_value) / 2, float(mode)]
