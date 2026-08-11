# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-11T21:14:11Z
# Experiment: ai-leetcode-lab, round 1
from typing import List
class Solution:
    def getSubarrayBeauty(self, nums: List[int], k: int, x: int) -> List[int]:
        count = [0] * 101; ans = []
        for i, value in enumerate(nums):
            count[value + 50] += 1
            if i >= k: count[nums[i - k] + 50] -= 1
            if i >= k - 1:
                remaining = x
                for value in range(-50, 0):
                    remaining -= count[value + 50]
                    if remaining <= 0: ans.append(value); break
                else: ans.append(0)
        return ans
