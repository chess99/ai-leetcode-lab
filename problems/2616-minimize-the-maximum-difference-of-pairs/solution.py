# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-11T21:01:28Z
# Experiment: ai-leetcode-lab, round 1
from typing import List


class Solution:
    def minimizeMax(self, nums: List[int], p: int) -> int:
        nums.sort()

        def can_make(limit: int) -> bool:
            pairs = 0
            index = 0
            while index + 1 < len(nums):
                if nums[index + 1] - nums[index] <= limit:
                    pairs += 1
                    index += 2
                else:
                    index += 1
            return pairs >= p

        left, right = 0, nums[-1] - nums[0]
        while left < right:
            middle = (left + right) // 2
            if can_make(middle):
                right = middle
            else:
                left = middle + 1
        return left
