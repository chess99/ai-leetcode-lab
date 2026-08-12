# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-12T06:02:51Z
# Experiment: ai-leetcode-lab, round 1
from typing import List


class Solution:
    def hitBricks(self, grid: List[List[int]], hits: List[List[int]]) -> List[int]:
        rows, columns = len(grid), len(grid[0]); roof = rows * columns
        parent = list(range(roof + 1)); size = [1] * (roof + 1); state = [row[:] for row in grid]
        effective = []
        for r,c in hits:
            removed = state[r][c] == 1
            effective.append(removed)
            if removed: state[r][c] = 0
        def find(x):
            while parent[x] != x: parent[x] = parent[parent[x]]; x = parent[x]
            return x
        def union(a,b):
            a,b=find(a),find(b)
            if a==b:return
            if size[a]<size[b]:a,b=b,a
            parent[b]=a;size[a]+=size[b]
        for r in range(rows):
            for c in range(columns):
                if state[r][c] != 1: continue
                x=r*columns+c
                if r==0:union(x,roof)
                if r and state[r-1][c]==1:union(x,(r-1)*columns+c)
                if c and state[r][c-1]==1:union(x,r*columns+c-1)
        answer=[]
        for (r,c), removed in zip(reversed(hits), reversed(effective)):
            if not removed: answer.append(0); continue
            before=size[find(roof)];state[r][c]=1;x=r*columns+c
            if r==0:union(x,roof)
            for nr,nc in ((r-1,c),(r+1,c),(r,c-1),(r,c+1)):
                if 0<=nr<rows and 0<=nc<columns and state[nr][nc]==1:union(x,nr*columns+nc)
            answer.append(max(0,size[find(roof)]-before-1))
        return answer[::-1]
