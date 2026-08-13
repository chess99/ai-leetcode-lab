# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-11T14:41:21Z
# Experiment: ai-leetcode-lab, round 1
from typing import List


class Solution:
    def isPossibleToSplit(self, nums: List[int]) -> bool:
        counts = {}
        for num in nums:
            counts[num] = counts.get(num, 0) + 1
            if counts[num] > 2:
                return False
        return True
