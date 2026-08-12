# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-12T14:40:29Z
# Experiment: ai-leetcode-lab, round 1
from collections import Counter
from typing import List


class Solution:
    def countSubarrays(self, nums: List[int], k: int) -> int:
        middle = nums.index(k)
        frequencies = Counter({0: 1})
        balance = 0
        for index in range(middle - 1, -1, -1):
            balance += 1 if nums[index] > k else -1
            frequencies[balance] += 1
        answer = 0
        balance = 0
        for index in range(middle, len(nums)):
            if index > middle:
                balance += 1 if nums[index] > k else -1
            answer += frequencies[-balance] + frequencies[1 - balance]
        return answer
