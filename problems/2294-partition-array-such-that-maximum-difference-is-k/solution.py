# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-11T20:21:24Z
# Experiment: ai-leetcode-lab, round 1

from typing import List


class Solution:
    def partitionArray(self, nums: List[int], k: int) -> int:
        nums.sort()
        groups = 1
        group_minimum = nums[0]

        for value in nums[1:]:
            if value - group_minimum > k:
                groups += 1
                group_minimum = value

        return groups
