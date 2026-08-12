# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-12T08:09:57Z
# Experiment: ai-leetcode-lab, round 1
from typing import List

class Solution:
    def minNumberOfSemesters(self, n: int, relations: List[List[int]], k: int) -> int:
        pre=[0]*n
        for a,b in relations:pre[b-1]|=1<<(a-1)
        dp=[n+1]*(1<<n);dp[0]=0
        for mask in range(1<<n):
            avail=0
            for i in range(n):
                if not mask>>i&1 and pre[i]&mask==pre[i]:avail|=1<<i
            sub=avail
            while sub:
                if sub.bit_count()<=k:dp[mask|sub]=min(dp[mask|sub],dp[mask]+1)
                sub=(sub-1)&avail
        return dp[-1]
