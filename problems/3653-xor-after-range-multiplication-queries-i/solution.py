# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-12T02:47:43Z
# Experiment: ai-leetcode-lab, round 1
from functools import reduce
from operator import xor
from typing import List

class Solution:
    def xorAfterQueries(self, nums: List[int], queries: List[List[int]]) -> int:
        mod = 10**9 + 7
        for left, right, step, value in queries:
            for index in range(left, right + 1, step):
                nums[index] = nums[index] * value % mod
        return reduce(xor, nums, 0)
