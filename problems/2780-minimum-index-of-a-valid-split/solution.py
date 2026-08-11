# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-11T21:14:14Z
# Experiment: ai-leetcode-lab, round 1
from collections import Counter
from typing import List
class Solution:
    def minimumIndex(self, nums: List[int]) -> int:
        total=Counter(nums); dom=max(total,key=total.get); seen=0
        for i,x in enumerate(nums[:-1]):
            seen+=x==dom
            if seen*2>i+1 and (total[dom]-seen)*2>len(nums)-i-1:return i
        return -1
