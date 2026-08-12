# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-12T12:52:04Z
# Experiment: ai-leetcode-lab, round 1
from typing import List


class Solution:
    def minOperations(self, nums: List[int]) -> int:
        a=sorted(set(nums)); n=len(nums); ans=n; j=0
        for i,x in enumerate(a):
            while j<len(a) and a[j]<x+n:j+=1
            ans=min(ans,n-(j-i))
        return ans
