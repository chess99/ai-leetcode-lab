# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-11T16:33:55Z
# Experiment: ai-leetcode-lab, round 1
from typing import List


class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        first = second = None
        first_count = second_count = 0
        for value in nums:
            if value == first: first_count += 1
            elif value == second: second_count += 1
            elif first_count == 0: first, first_count = value, 1
            elif second_count == 0: second, second_count = value, 1
            else: first_count -= 1; second_count -= 1
        return [value for value in (first, second) if value is not None and nums.count(value) > len(nums) // 3]
