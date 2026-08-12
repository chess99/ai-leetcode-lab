# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-12T17:28:47Z
# Experiment: ai-leetcode-lab, round 1
from typing import List


class Solution:
    def countStableSubsequences(self, nums: List[int]) -> int:
        mod=1_000_000_007;dp=[[0,0]for _ in range(2)]
        for x in nums:
            p=x&1;nd=[z[:]for z in dp]
            nd[p][0]=(nd[p][0]+1+dp[1-p][0]+dp[1-p][1])%mod
            nd[p][1]=(nd[p][1]+dp[p][0])%mod
            dp=nd
        return sum(map(sum,dp))%mod
