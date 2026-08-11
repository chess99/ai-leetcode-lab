# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-11T18:05:42Z
# Experiment: ai-leetcode-lab, round 1
from typing import List


class Solution:
    def sumEvenAfterQueries(self, nums: List[int], queries: List[List[int]]) -> List[int]:
        even_sum = sum(value for value in nums if value % 2 == 0)
        result = []
        for value, index in queries:
            if nums[index] % 2 == 0:
                even_sum -= nums[index]
            nums[index] += value
            if nums[index] % 2 == 0:
                even_sum += nums[index]
            result.append(even_sum)
        return result
