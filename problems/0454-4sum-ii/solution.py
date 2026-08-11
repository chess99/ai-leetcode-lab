# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-11T17:06:35Z
# Experiment: ai-leetcode-lab, round 1
from collections import Counter
from typing import List


class Solution:
    def fourSumCount(self, nums1: List[int], nums2: List[int], nums3: List[int], nums4: List[int]) -> int:
        pair_sums = Counter(a + b for a in nums1 for b in nums2)
        return sum(pair_sums[-(c + d)] for c in nums3 for d in nums4)
