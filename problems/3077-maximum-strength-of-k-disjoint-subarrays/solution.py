# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-12T15:15:55Z
# Experiment: ai-leetcode-lab, round 1
from typing import List
class Solution:
    def maximumStrength(self, nums: List[int], k: int) -> int:
        neg=-10**30;end=[neg]*(k+1);best=[neg]*(k+1);best[0]=0
        for x in nums:
            for j in range(k,0,-1):
                c=(k-j+1)*(1 if j%2 else -1);end[j]=max(end[j]+c*x,best[j-1]+c*x);best[j]=max(best[j],end[j])
        return best[k]
