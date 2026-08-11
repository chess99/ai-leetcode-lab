# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-11T22:15:54Z
# Experiment: ai-leetcode-lab, round 1
from typing import List

class Solution:
    def minSwaps(self, nums: List[int]) -> int:
        def digit_sum(x: int) -> int:
            return sum(map(int, str(x)))
        target = sorted(nums, key=lambda x: (digit_sum(x), x))
        pos = {value: i for i, value in enumerate(nums)}
        swaps = 0
        for i, value in enumerate(target):
            if nums[i] != value:
                j = pos[value]
                pos[nums[i]] = j
                nums[i], nums[j] = nums[j], nums[i]
                swaps += 1
        return swaps
