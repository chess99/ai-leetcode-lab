# AI solution attribution
# Client: Codex Desktop
# Model: GPT-5
# Created: 2026-08-11T09:03:57Z
# Experiment: ai-leetcode-lab, round 1
from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen: dict[int, int] = {}

        for index, value in enumerate(nums):
            complement = target - value
            if complement in seen:
                return [seen[complement], index]
            seen[value] = index

        return []
