# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-11T21:14:11Z
# Experiment: ai-leetcode-lab, round 1
from typing import List
class Solution:
    def findMaxFish(self, grid: List[List[int]]) -> int:
        m, n, answer = len(grid), len(grid[0]), 0
        for r in range(m):
            for c in range(n):
                if grid[r][c]:
                    stack, total = [(r,c)], 0
                    while stack:
                        x,y=stack.pop()
                        if not (0<=x<m and 0<=y<n) or grid[x][y]==0: continue
                        total += grid[x][y]; grid[x][y]=0
                        stack += [(x-1,y),(x+1,y),(x,y-1),(x,y+1)]
                    answer=max(answer,total)
        return answer
