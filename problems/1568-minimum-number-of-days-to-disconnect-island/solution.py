# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-12T08:10:00Z
# Experiment: ai-leetcode-lab, round 1
from typing import List

class Solution:
    def minDays(self, grid: List[List[int]]) -> int:
        def islands():
            seen=set();count=0
            for r in range(len(grid)):
                for c in range(len(grid[0])):
                    if grid[r][c] and (r,c) not in seen:
                        count+=1;stack=[(r,c)];seen.add((r,c))
                        while stack:
                            x,y=stack.pop()
                            for a,b in ((x+1,y),(x-1,y),(x,y+1),(x,y-1)):
                                if 0<=a<len(grid) and 0<=b<len(grid[0]) and grid[a][b] and (a,b)not in seen:seen.add((a,b));stack.append((a,b))
            return count
        if islands()!=1:return 0
        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if grid[r][c]:
                    grid[r][c]=0
                    if islands()!=1:return 1
                    grid[r][c]=1
        return 2
