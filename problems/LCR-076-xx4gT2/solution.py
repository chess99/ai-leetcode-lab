# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-12T04:46:16Z
# Experiment: ai-leetcode-lab, round 1
from typing import List


class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        target = len(nums) - k
        left, right = 0, len(nums) - 1
        while left <= right:
            pivot = nums[(left + right) // 2]
            low, current, high = left, left, right
            while current <= high:
                if nums[current] < pivot:
                    nums[low], nums[current] = nums[current], nums[low]
                    low += 1
                    current += 1
                elif nums[current] > pivot:
                    nums[current], nums[high] = nums[high], nums[current]
                    high -= 1
                else:
                    current += 1
            if target < low:
                right = low - 1
            elif target > high:
                left = high + 1
            else:
                return pivot
