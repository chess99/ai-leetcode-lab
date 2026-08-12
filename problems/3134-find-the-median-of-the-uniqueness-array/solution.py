# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-12T15:15:58Z
# Experiment: ai-leetcode-lab, round 1
from collections import defaultdict
from typing import List


class Solution:
    def medianOfUniquenessArray(self, nums: List[int]) -> int:
        size = len(nums)
        target = (size * (size + 1) // 2 + 1) // 2

        def count(maximum_unique):
            frequencies = defaultdict(int)
            distinct = 0
            left = 0
            total = 0
            for right, value in enumerate(nums):
                if frequencies[value] == 0:
                    distinct += 1
                frequencies[value] += 1
                while distinct > maximum_unique:
                    removed = nums[left]
                    frequencies[removed] -= 1
                    if frequencies[removed] == 0:
                        distinct -= 1
                    left += 1
                total += right - left + 1
            return total

        low, high = 1, len(set(nums))
        while low < high:
            middle = (low + high) // 2
            if count(middle) >= target:
                high = middle
            else:
                low = middle + 1
        return low
