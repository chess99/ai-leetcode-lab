# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-11T20:37:14Z
# Experiment: ai-leetcode-lab, round 1
from typing import List
class Solution:
    def smallestSubarrays(self, nums: List[int]) -> List[int]:
        last = [-1] * 32; answer = [1] * len(nums)
        for index in range(len(nums) - 1, -1, -1):
            for bit in range(32):
                if nums[index] & (1 << bit): last[bit] = index
            answer[index] = max(index, max(last)) - index + 1
        return answer
