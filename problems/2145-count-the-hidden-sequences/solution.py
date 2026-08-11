# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-11T20:05:28Z
# Experiment: ai-leetcode-lab, round 1
from typing import List


class Solution:
    def numberOfArrays(self, differences: List[int], lower: int, upper: int) -> int:
        prefix = 0
        minimum = 0
        maximum = 0
        for difference in differences:
            prefix += difference
            minimum = min(minimum, prefix)
            maximum = max(maximum, prefix)
        return max(0, (upper - lower + 1) - (maximum - minimum))
