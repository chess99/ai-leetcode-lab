# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-12T14:40:44Z
# Experiment: ai-leetcode-lab, round 1
from collections import defaultdict
from typing import List


class Solution:
    def maximumSum(self, nums: List[int]) -> int:
        sums = defaultdict(int)
        for index, value in enumerate(nums, 1):
            kernel = index
            divisor = 2
            while divisor * divisor <= kernel:
                while kernel % (divisor * divisor) == 0:
                    kernel //= divisor * divisor
                divisor += 1
            sums[kernel] += value
        return max(sums.values())
