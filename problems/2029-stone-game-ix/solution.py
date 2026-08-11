# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-11T19:48:14Z
# Experiment: ai-leetcode-lab, round 1
from typing import List


class Solution:
    def stoneGameIX(self, stones: List[int]) -> bool:
        remainder_count = [0, 0, 0]
        for stone in stones:
            remainder_count[stone % 3] += 1

        zero, one, two = remainder_count
        if zero % 2 == 0:
            return one > 0 and two > 0
        return abs(one - two) > 2
