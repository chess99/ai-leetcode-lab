# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-12T13:47:49Z
# Experiment: ai-leetcode-lab, round 1
from typing import List


class Solution:
    def minOperations(self, nums: List[int], numsDivide: List[int]) -> int:
        from math import gcd
        g=0
        for x in numsDivide:g=gcd(g,x)
        for i,x in enumerate(sorted(nums)):
            if g%x==0:return i
        return -1
