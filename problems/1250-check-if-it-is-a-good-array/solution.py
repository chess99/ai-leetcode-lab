# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-12T06:20:12Z
# Experiment: ai-leetcode-lab, round 1
from typing import List


class Solution:
    def isGoodArray(self, nums: List[int]) -> bool:
        from math import gcd
        value=0
        for x in nums:value=gcd(value,x)
        return value==1
