# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-12T06:20:04Z
# Experiment: ai-leetcode-lab, round 1
from typing import List


class Solution:
    def minDeletionSize(self, strs: List[str]) -> int:
        n=len(strs[0]);dp=[1]*n
        for j in range(n):
            for i in range(j):
                if all(row[i]<=row[j]for row in strs):dp[j]=max(dp[j],dp[i]+1)
        return n-max(dp)
