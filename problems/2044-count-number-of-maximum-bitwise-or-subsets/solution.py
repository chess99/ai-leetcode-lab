# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-11T20:05:18Z
# Experiment: ai-leetcode-lab, round 1
from typing import List


class Solution:
    def countMaxOrSubsets(self, nums: List[int]) -> int:
        maximum = 0
        for value in nums:
            maximum |= value

        count = 0

        def search(index: int, current: int) -> None:
            nonlocal count
            if index == len(nums):
                count += current == maximum
                return
            search(index + 1, current)
            search(index + 1, current | nums[index])

        search(0, 0)
        return count
