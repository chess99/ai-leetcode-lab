# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-11T21:14:15Z
# Experiment: ai-leetcode-lab, round 1
from collections import defaultdict
from typing import List
class Solution:
    def minimumSeconds(self, nums: List[int]) -> int:
        pos=defaultdict(list); n=len(nums)
        for i,x in enumerate(nums):pos[x].append(i)
        ans=n
        for ids in pos.values():
            gap=max(b-a for a,b in zip(ids,ids[1:]))
            gap=max(gap,ids[0]+n-ids[-1]); ans=min(ans,gap//2)
        return ans
