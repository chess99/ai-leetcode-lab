# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-12T08:09:48Z
# Experiment: ai-leetcode-lab, round 1
from collections import deque
from typing import List

class Solution:
    def shortestPath(self, grid: List[List[int]], k: int) -> int:
        rows,columns=len(grid),len(grid[0])
        if k>=rows+columns-2:return rows+columns-2
        queue=deque([(0,0,k,0)]);best={(0,0):k}
        while queue:
            row,column,left,distance=queue.popleft()
            if (row,column)==(rows-1,columns-1):return distance
            for rr,cc in ((row-1,column),(row+1,column),(row,column-1),(row,column+1)):
                if 0<=rr<rows and 0<=cc<columns:
                    remaining=left-grid[rr][cc]
                    if remaining>=0 and remaining>best.get((rr,cc),-1):best[rr,cc]=remaining;queue.append((rr,cc,remaining,distance+1))
        return -1
