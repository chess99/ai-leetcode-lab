# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-11T21:14:14Z
# Experiment: ai-leetcode-lab, round 1
from typing import List
class Solution:
    def maxScore(self, nums: List[int], x: int) -> int:
        even=odd=-10**30
        for v in nums:
            if v%2: odd=max(odd+v,even+v-x,v)
            else: even=max(even+v,odd+v-x,v)
        return max(even,odd)
