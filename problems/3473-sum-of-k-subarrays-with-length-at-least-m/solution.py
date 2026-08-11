# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-11T21:59:19Z
# Experiment: ai-leetcode-lab, round 1
from typing import List
class Solution:
    def maxSum(self, nums: List[int], k: int, m: int) -> int:
        n=len(nums); prefix=[0]
        for x in nums: prefix.append(prefix[-1]+x)
        neg=-10**30; prev=[0]*(n+1)
        for count in range(1,k+1):
            cur=[neg]*(n+1); best=neg
            for i in range(1,n+1):
                if i>=m: best=max(best,prev[i-m]-prefix[i-m])
                cur[i]=max(cur[i-1],prefix[i]+best)
            prev=cur
        return prev[n]
