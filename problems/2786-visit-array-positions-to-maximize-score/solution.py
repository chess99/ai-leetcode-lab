# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-11T21:14:14Z
# Experiment: ai-leetcode-lab, round 1
from typing import List
class Solution:
    def maxScore(self, nums: List[int], x: int) -> int:
        even = odd = -10**30
        if nums[0] % 2:
            odd = nums[0]
        else:
            even = nums[0]
        for v in nums[1:]:
            if v % 2:
                odd = max(odd + v, even + v - x)
            else:
                even = max(even + v, odd + v - x)
        return max(even,odd)
