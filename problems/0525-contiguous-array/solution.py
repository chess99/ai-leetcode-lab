# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-11T17:13:38Z
# Experiment: ai-leetcode-lab, round 1
from typing import List


class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        first_index = {0: -1}
        balance = 0
        longest = 0
        for index, number in enumerate(nums):
            balance += 1 if number == 1 else -1
            if balance in first_index:
                longest = max(longest, index - first_index[balance])
            else:
                first_index[balance] = index
        return longest
