# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-11T17:24:42Z
# Experiment: ai-leetcode-lab, round 1
from typing import List


class Solution:
    def triangleNumber(self, nums: List[int]) -> int:
        nums.sort()
        count = 0
        for longest in range(len(nums) - 1, 1, -1):
            left, right = 0, longest - 1
            while left < right:
                if nums[left] + nums[right] > nums[longest]:
                    count += right - left
                    right -= 1
                else:
                    left += 1
        return count
