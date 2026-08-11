# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-11T21:01:27Z
# Experiment: ai-leetcode-lab, round 1
from collections import Counter
from typing import List


class Solution:
    def findSmallestInteger(self, nums: List[int], value: int) -> int:
        remaining = Counter(num % value for num in nums)
        mex = 0
        while remaining[mex % value]:
            remaining[mex % value] -= 1
            mex += 1
        return mex
