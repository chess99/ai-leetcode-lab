# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-11T20:05:23Z
# Experiment: ai-leetcode-lab, round 1

from typing import List


class Solution:
    def minimumDeletions(self, nums: List[int]) -> int:
        minimum_index = nums.index(min(nums))
        maximum_index = nums.index(max(nums))
        left = min(minimum_index, maximum_index)
        right = max(minimum_index, maximum_index)

        return min(
            right + 1,
            len(nums) - left,
            left + 1 + len(nums) - right,
        )
