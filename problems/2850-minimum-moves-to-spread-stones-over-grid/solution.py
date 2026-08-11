# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-11T21:23:06Z
# Experiment: ai-leetcode-lab, round 1
from functools import lru_cache
from typing import List
class Solution:
    def minimumMoves(self, grid: List[List[int]]) -> int:
        extra=[]; empty=[]
        for i in range(3):
            for j in range(3):
                if grid[i][j]==0: empty.append((i,j))
                else: extra += [(i,j)]*(grid[i][j]-1)
        @lru_cache(None)
        def dfs(i, mask):
            if i==len(extra): return 0
            return min(abs(extra[i][0]-empty[j][0])+abs(extra[i][1]-empty[j][1])+dfs(i+1,mask|1<<j) for j in range(len(empty)) if not mask>>j&1)
        return dfs(0,0)
