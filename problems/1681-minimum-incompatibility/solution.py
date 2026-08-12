# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-12T11:06:37Z
# Experiment: ai-leetcode-lab, round 1
from typing import List


class Solution:
    def minimumIncompatibility(self, nums: List[int], k: int) -> int:
        from collections import Counter
        if max(Counter(nums).values())>k:return -1
        n=len(nums);size=n//k;cost={}
        for m in range(1,1<<n):
            if m.bit_count()==size:
                a=[nums[i]for i in range(n)if m>>i&1]
                if len(set(a))==size:cost[m]=max(a)-min(a)
        dp={0:0}
        for mask in range(1<<n):
            if mask not in dp:continue
            first=next((i for i in range(n)if not mask>>i&1),None)
            if first is None:continue
            for sub,v in cost.items():
                if sub>>first&1 and not sub&mask:dp[mask|sub]=min(dp.get(mask|sub,10**9),dp[mask]+v)
        return dp.get((1<<n)-1,-1)
