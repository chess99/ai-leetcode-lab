# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-11T14:45:49Z
# Experiment: ai-leetcode-lab, round 1
# Handoff: fixed by sol-medium (gpt-5.6-sol / medium)
from typing import List


class Solution:
    def numberOfPairs(self, nums1: List[int], nums2: List[int], k: int) -> int:
        return sum(a % (b * k) == 0 for a in nums1 for b in nums2)
