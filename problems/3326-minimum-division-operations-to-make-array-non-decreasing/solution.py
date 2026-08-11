# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-11T21:46:17Z
# Experiment: ai-leetcode-lab, round 1
from typing import List

class Solution:
    def minOperations(self, nums: List[int]) -> int:
        def smallest_prime_factor(value: int) -> int:
            divisor = 2
            while divisor * divisor <= value:
                if value % divisor == 0:
                    return divisor
                divisor += 1
            return value
        operations = 0
        for i in range(len(nums) - 2, -1, -1):
            if nums[i] > nums[i + 1]:
                nums[i] = smallest_prime_factor(nums[i])
                operations += 1
                if nums[i] > nums[i + 1]:
                    return -1
        return operations
