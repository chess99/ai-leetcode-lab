# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-11T16:10:38Z
# Experiment: ai-leetcode-lab, round 1
from typing import List


class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        def boundary(find_first: bool) -> int:
            left, right = 0, len(nums) - 1
            result = -1
            while left <= right:
                middle = (left + right) // 2
                if nums[middle] == target:
                    result = middle
                    if find_first:
                        right = middle - 1
                    else:
                        left = middle + 1
                elif nums[middle] < target:
                    left = middle + 1
                else:
                    right = middle - 1
            return result

        return [boundary(True), boundary(False)]
