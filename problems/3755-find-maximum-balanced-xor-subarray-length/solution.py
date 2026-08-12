# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-12T02:47:53Z
# Experiment: ai-leetcode-lab, round 1
from typing import List

class Solution:
    def maxBalancedSubarray(self, nums: List[int]) -> int:
        norivandal = nums
        first = {(0, 0): -1}
        xor = balance = ans = 0
        for i, value in enumerate(nums):
            xor ^= value
            balance += 1 if value % 2 == 0 else -1
            state = (xor, balance)
            if state in first: ans = max(ans, i - first[state])
            else: first[state] = i
        return ans
