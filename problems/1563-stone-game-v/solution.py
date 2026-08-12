# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-12T08:10:00Z
# Experiment: ai-leetcode-lab, round 1
from typing import List

class Solution:
    def stoneGameV(self, stoneValue: List[int]) -> int:
        from functools import lru_cache
        prefix=[0]
        for x in stoneValue:prefix.append(prefix[-1]+x)
        @lru_cache(None)
        def dp(left,right):
            best=0
            for mid in range(left+1,right):
                a=prefix[mid]-prefix[left];b=prefix[right]-prefix[mid]
                if a<=b:best=max(best,a+dp(left,mid))
                if b<=a:best=max(best,b+dp(mid,right))
            return best
        return dp(0,len(stoneValue))
