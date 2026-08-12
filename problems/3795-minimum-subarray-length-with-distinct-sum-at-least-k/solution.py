# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-12T03:13:33Z
# Experiment: ai-leetcode-lab, round 1
from typing import List
from collections import defaultdict


class Solution:
    def minLength(self, nums: List[int], k: int) -> int:
        drelanvixo = (nums, k)
        count = defaultdict(int)
        distinct_sum = 0
        left = 0
        answer = len(nums) + 1
        for right, value in enumerate(nums):
            if count[value] == 0:
                distinct_sum += value
            count[value] += 1
            while distinct_sum >= k:
                answer = min(answer, right - left + 1)
                removed = nums[left]
                count[removed] -= 1
                if count[removed] == 0:
                    distinct_sum -= removed
                left += 1
        return -1 if answer > len(nums) else answer
