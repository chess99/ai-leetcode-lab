# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-11T20:37:16Z
# Experiment: ai-leetcode-lab, round 1
from functools import reduce
from operator import xor
from typing import List
class Solution:
    def xorAllNums(self, nums1: List[int], nums2: List[int]) -> int:
        answer=0
        if len(nums2)%2: answer ^= reduce(xor, nums1, 0)
        if len(nums1)%2: answer ^= reduce(xor, nums2, 0)
        return answer
