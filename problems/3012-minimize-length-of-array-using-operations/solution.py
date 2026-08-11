# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-11T21:34:36Z
# Experiment: ai-leetcode-lab, round 1
from typing import List


class Solution:
    def minimumArrayLength(self, nums: List[int]) -> int:
        smallest = min(nums)
        if any(num % smallest for num in nums):
            return 1
        return (nums.count(smallest) + 1) // 2
