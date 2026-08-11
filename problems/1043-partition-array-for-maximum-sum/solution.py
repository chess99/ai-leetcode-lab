# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-11T18:13:29Z
# Experiment: ai-leetcode-lab, round 1
from typing import List
class Solution:
    def maxSumAfterPartitioning(self, arr: List[int], k: int) -> int:
        dp=[0]*(len(arr)+1)
        for i in range(1,len(arr)+1):
            maximum=0
            for length in range(1,min(k,i)+1): maximum=max(maximum,arr[i-length]);dp[i]=max(dp[i],dp[i-length]+maximum*length)
        return dp[-1]
