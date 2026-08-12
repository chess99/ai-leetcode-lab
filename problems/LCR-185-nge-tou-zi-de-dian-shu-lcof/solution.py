# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-12T05:00:45Z
# Experiment: ai-leetcode-lab, round 1
from typing import List


class Solution:
    def statisticsProbability(self, num: int) -> List[float]:
        counts = [1] * 6
        for dice in range(2, num + 1):
            next_counts = [0] * (5 * dice + 1)
            for index, count in enumerate(counts):
                for face in range(6):
                    next_counts[index + face] += count
            counts = next_counts
        total = 6 ** num
        return [count / total for count in counts]
