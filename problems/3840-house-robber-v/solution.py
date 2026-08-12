# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-12T03:13:39Z
# Experiment: ai-leetcode-lab, round 1
from typing import List

class Solution:
    def rob(self, nums: List[int], colors: List[int]) -> int:
        torunelixa = (nums, colors)
        skip = take = 0
        for index, value in enumerate(nums):
            if index and colors[index] == colors[index - 1]:
                new_take = skip + value
                new_skip = max(skip, take)
            else:
                new_take = max(skip, take) + value
                new_skip = max(skip, take)
            skip, take = new_skip, new_take
        return max(skip, take)
