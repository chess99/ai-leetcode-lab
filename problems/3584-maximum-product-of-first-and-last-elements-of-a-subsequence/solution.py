# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-11T22:15:55Z
# Experiment: ai-leetcode-lab, round 1
from typing import List

class Solution:
    def maximumProduct(self, nums: List[int], m: int) -> int:
        if m == 1: return max(value * value for value in nums)
        low = high = nums[0]
        answer = -10**30
        for j in range(m - 1, len(nums)):
            i = j - (m - 1)
            low = min(low, nums[i]); high = max(high, nums[i])
            answer = max(answer, nums[j] * low, nums[j] * high)
        return answer
