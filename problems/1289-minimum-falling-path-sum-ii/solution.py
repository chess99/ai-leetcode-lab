# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-12T08:09:47Z
# Experiment: ai-leetcode-lab, round 1
from typing import List

class Solution:
    def minFallingPathSum(self, grid: List[List[int]]) -> int:
        dp=grid[0][:]
        for row in grid[1:]:
            first=min(range(len(dp)),key=dp.__getitem__);second=min((i for i in range(len(dp)) if i!=first),key=dp.__getitem__)
            dp=[value+dp[second if column==first else first] for column,value in enumerate(row)]
        return min(dp)
