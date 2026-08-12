# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-12T14:40:35Z
# Experiment: ai-leetcode-lab, round 1
from typing import List
class Solution:
    def waysToReachTarget(self, target: int, types: List[List[int]]) -> int:
        mod=10**9+7;dp=[0]*(target+1);dp[0]=1
        for count,score in types:
            nd=[0]*(target+1)
            for i in range(target+1):
                for q in range(count+1):
                    if i+q*score<=target:nd[i+q*score]=(nd[i+q*score]+dp[i])%mod
            dp=nd
        return dp[target]
