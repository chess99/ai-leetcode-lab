# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-11T21:01:26Z
# Experiment: ai-leetcode-lab, round 1
from typing import List


class Solution:
    def countFairPairs(self, nums: List[int], lower: int, upper: int) -> int:
        nums.sort()

        def count_at_most(limit: int) -> int:
            left, right, count = 0, len(nums) - 1, 0
            while left < right:
                if nums[left] + nums[right] <= limit:
                    count += right - left
                    left += 1
                else:
                    right -= 1
            return count

        return count_at_most(upper) - count_at_most(lower - 1)
