# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-12T04:46:21Z
# Experiment: ai-leetcode-lab, round 1
from typing import List


class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]

        def rob_line(left: int, right: int) -> int:
            previous = current = 0
            for index in range(left, right):
                previous, current = current, max(current, previous + nums[index])
            return current

        return max(rob_line(0, len(nums) - 1), rob_line(1, len(nums)))
