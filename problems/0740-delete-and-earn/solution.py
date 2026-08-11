# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-11T17:41:41Z
# Experiment: ai-leetcode-lab, round 1
from collections import Counter
from typing import List


class Solution:
    def deleteAndEarn(self, nums: List[int]) -> int:
        points = Counter(nums)
        take = skip = 0
        previous = -1
        for value in sorted(points):
            gain = value * points[value]
            if value == previous + 1:
                take, skip = skip + gain, max(take, skip)
            else:
                take, skip = max(take, skip) + gain, max(take, skip)
            previous = value
        return max(take, skip)
