# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-12T06:02:55Z
# Experiment: ai-leetcode-lab, round 1
from collections import deque
from typing import List


class Solution:
    def shortestPathAllKeys(self, grid: List[str]) -> int:
        rows,columns=len(grid),len(grid[0]);keys={c for row in grid for c in row if c.islower()};target=(1<<len(keys))-1;mapping={c:i for i,c in enumerate(sorted(keys))}
        for r,row in enumerate(grid):
            if '@' in row:start=(r,row.index('@'))
        queue=deque([(start[0],start[1],0,0)]);seen={(start[0],start[1],0)}
        while queue:
            r,c,mask,distance=queue.popleft()
            if mask==target:return distance
            for nr,nc in ((r-1,c),(r+1,c),(r,c-1),(r,c+1)):
                if not(0<=nr<rows and 0<=nc<columns)or grid[nr][nc]=='#':continue
                char=grid[nr][nc];new_mask=mask
                if char.islower():new_mask|=1<<mapping[char]
                if char.isupper() and (char.lower() not in mapping or not(new_mask>>mapping[char.lower()]&1)):continue
                state=(nr,nc,new_mask)
                if state not in seen:seen.add(state);queue.append((nr,nc,new_mask,distance+1))
        return -1
