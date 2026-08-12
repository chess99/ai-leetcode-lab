# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-12T04:15:21Z
# Experiment: ai-leetcode-lab, round 1
from typing import List


class Solution:
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
        if k <= 1:
            return 0
        product_value = 1
        left = answer = 0
        for right, value in enumerate(nums):
            product_value *= value
            while product_value >= k:
                product_value //= nums[left]
                left += 1
            answer += right - left + 1
        return answer
