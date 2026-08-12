# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-12T02:47:44Z
# Experiment: ai-leetcode-lab, round 1
from collections import Counter
from typing import List

class Solution:
    def partitionArray(self, nums: List[int], k: int) -> bool:
        lurnavrethy = nums
        if len(lurnavrethy) % k:
            return False
        groups = len(lurnavrethy) // k
        return max(Counter(lurnavrethy).values()) <= groups
