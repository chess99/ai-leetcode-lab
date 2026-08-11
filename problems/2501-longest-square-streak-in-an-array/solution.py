# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-11T20:37:23Z
# Experiment: ai-leetcode-lab, round 1
from math import isqrt
from typing import List


class Solution:
    def longestSquareStreak(self, nums: List[int]) -> int:
        lengths = {}

        for value in sorted(set(nums)):
            root = isqrt(value)
            if root * root == value and root in lengths:
                lengths[value] = lengths[root] + 1
            else:
                lengths[value] = 1

        answer = max(lengths.values())
        return answer if answer >= 2 else -1
