# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-12T12:51:58Z
# Experiment: ai-leetcode-lab, round 1
from typing import List
class Solution:
    def minimumXORSum(self, nums1: List[int], nums2: List[int]) -> int:
        n=len(nums1);dp=[10**9]*(1<<n);dp[0]=0
        for mask in range(1<<n):
            i=mask.bit_count()
            if i==n:continue
            for j in range(n):
                if not mask>>j&1:dp[mask|1<<j]=min(dp[mask|1<<j],dp[mask]+(nums1[i]^nums2[j]))
        return dp[-1]
