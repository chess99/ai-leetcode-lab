# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-11T19:14:56Z
# Experiment: ai-leetcode-lab, round 1
from typing import List
class Solution:
    def containsCycle(self, grid: List[List[str]]) -> bool:
        rows, cols = len(grid), len(grid[0]); seen=set()
        for start_row in range(rows):
            for start_col in range(cols):
                if (start_row,start_col) in seen: continue
                stack=[(start_row,start_col,-1,-1)];seen.add((start_row,start_col))
                while stack:
                    row,col,parent_row,parent_col=stack.pop()
                    for dr,dc in ((1,0),(-1,0),(0,1),(0,-1)):
                        nr,nc=row+dr,col+dc
                        if not (0<=nr<rows and 0<=nc<cols) or grid[nr][nc]!=grid[row][col] or (nr,nc)==(parent_row,parent_col): continue
                        if (nr,nc) in seen: return True
                        seen.add((nr,nc));stack.append((nr,nc,row,col))
        return False
