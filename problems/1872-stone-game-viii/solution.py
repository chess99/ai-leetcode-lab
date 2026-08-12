# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-12T11:06:49Z
# Experiment: ai-leetcode-lab, round 1
from typing import List


class Solution:
    def stoneGameVIII(self, stones: List[int]) -> int:
        prefix = []
        total = 0
        for stone in stones:
            total += stone
            prefix.append(total)
        difference = prefix[-1]
        for index in range(len(stones) - 2, 0, -1):
            difference = max(difference, prefix[index] - difference)
        return difference
