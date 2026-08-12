# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-12T17:28:46Z
# Experiment: ai-leetcode-lab, round 1
from typing import List


class Solution:
    def maxXorSubsequences(self, nums: List[int]) -> int:
        basis=[0]*31
        for x in nums:
            for b in range(30,-1,-1):
                if not x>>b&1:continue
                if basis[b]:x^=basis[b]
                else:basis[b]=x;break
        ans=0
        for x in basis:ans=max(ans,ans^x)
        return ans
