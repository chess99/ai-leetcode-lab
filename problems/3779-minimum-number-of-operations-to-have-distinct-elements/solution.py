# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-12T03:13:31Z
# Experiment: ai-leetcode-lab, round 1
from typing import List


class Solution:
    def minOperations(self, nums: List[int]) -> int:
        seen = set()
        for index in range(len(nums) - 1, -1, -1):
            if nums[index] in seen:
                return (index + 3) // 3
            seen.add(nums[index])
        return 0
