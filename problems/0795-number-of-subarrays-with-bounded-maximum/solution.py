# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-11T17:46:07Z
# Experiment: ai-leetcode-lab, round 1
from typing import List
class Solution:
    def numSubarrayBoundedMax(self, nums: List[int], left: int, right: int) -> int:
        def count(bound):
            total = run = 0
            for n in nums: run = run + 1 if n <= bound else 0; total += run
            return total
        return count(right) - count(left - 1)
