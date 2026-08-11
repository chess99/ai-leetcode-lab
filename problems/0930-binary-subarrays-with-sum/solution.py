# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-11T17:58:56Z
# Experiment: ai-leetcode-lab, round 1
from collections import defaultdict
from typing import List


class Solution:
    def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:
        frequencies = defaultdict(int)
        frequencies[0] = 1
        prefix = 0
        count = 0
        for value in nums:
            prefix += value
            count += frequencies[prefix - goal]
            frequencies[prefix] += 1
        return count
