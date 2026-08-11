# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-11T20:05:25Z
# Experiment: ai-leetcode-lab, round 1
from typing import List


class Solution:
    def getDescentPeriods(self, prices: List[int]) -> int:
        total = 1
        length = 1

        for i in range(1, len(prices)):
            if prices[i - 1] - prices[i] == 1:
                length += 1
            else:
                length = 1
            total += length

        return total
