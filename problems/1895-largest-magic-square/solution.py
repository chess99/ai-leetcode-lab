# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-11T19:47:30Z
# Experiment: ai-leetcode-lab, round 1
from typing import List
class Solution:
    def largestMagicSquare(self, grid: List[List[int]]) -> int:
        rows,cols=len(grid),len(grid[0]);row=[[0]*(cols+1) for _ in range(rows+1)];col=[[0]*(cols+1) for _ in range(rows+1)]
        for r in range(rows):
            for c in range(cols):row[r+1][c+1]=row[r+1][c]+grid[r][c];col[r+1][c+1]=col[r][c+1]+grid[r][c]
        for size in range(min(rows,cols),0,-1):
            for r in range(rows-size+1):
                for c in range(cols-size+1):
                    target=row[r+1][c+size]-row[r+1][c]
                    if all(row[x+1][c+size]-row[x+1][c]==target for x in range(r,r+size)) and all(col[r+size][y+1]-col[r][y+1]==target for y in range(c,c+size)) and sum(grid[r+i][c+i] for i in range(size))==target and sum(grid[r+i][c+size-1-i] for i in range(size))==target:return size
        return 1
