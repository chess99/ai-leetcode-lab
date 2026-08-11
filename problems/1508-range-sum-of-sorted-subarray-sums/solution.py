# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-11T18:54:21Z
# Experiment: ai-leetcode-lab, round 1
from typing import List

class Solution:
    def rangeSum(self, nums: List[int], n: int, left: int, right: int) -> int:
        sums = []
        for start in range(n):
            total = 0
            for end in range(start, n): total += nums[end]; sums.append(total)
        sums.sort()
        return sum(sums[left - 1:right]) % (10 ** 9 + 7)
