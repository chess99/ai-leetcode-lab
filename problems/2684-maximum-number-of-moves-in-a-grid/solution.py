# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-11T21:14:12Z
# Experiment: ai-leetcode-lab, round 1
from typing import List
class Solution:
    def maxMoves(self, grid: List[List[int]]) -> int:
        m,n=len(grid),len(grid[0]); reachable=set(range(m))
        for col in range(n-1):
            nxt={r2 for r in reachable for r2 in (r-1,r,r+1) if 0<=r2<m and grid[r2][col+1]>grid[r][col]}
            if not nxt: return col
            reachable=nxt
        return n-1
