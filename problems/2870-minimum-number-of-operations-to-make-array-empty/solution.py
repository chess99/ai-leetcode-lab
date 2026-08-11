# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-11T21:23:07Z
# Experiment: ai-leetcode-lab, round 1
from collections import Counter
from typing import List


class Solution:
    def minOperations(self, nums: List[int]) -> int:
        operations = 0
        for count in Counter(nums).values():
            if count == 1:
                return -1
            operations += (count + 2) // 3
        return operations
