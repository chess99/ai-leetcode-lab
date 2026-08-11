# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-11T18:53:33Z
# Experiment: ai-leetcode-lab, round 1
from typing import List


class Solution:
    def numSubseq(self, nums: List[int], target: int) -> int:
        modulo = 1_000_000_007
        nums.sort()
        powers_of_two = [1] * len(nums)
        for index in range(1, len(nums)):
            powers_of_two[index] = (powers_of_two[index - 1] * 2) % modulo

        left, right = 0, len(nums) - 1
        count = 0
        while left <= right:
            if nums[left] + nums[right] <= target:
                count = (count + powers_of_two[right - left]) % modulo
                left += 1
            else:
                right -= 1

        return count
