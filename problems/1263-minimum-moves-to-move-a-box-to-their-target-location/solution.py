# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-12T06:20:13Z
# Experiment: ai-leetcode-lab, round 1
from typing import List


class Solution:
    def minPushBox(self, grid: List[List[str]]) -> int:
        from collections import deque
        rows,cols=len(grid),len(grid[0])
        for r in range(rows):
            for c in range(cols):
                if grid[r][c]=='S':player=(r,c)
                elif grid[r][c]=='B':box=(r,c)
                elif grid[r][c]=='T':target=(r,c)
        queue=deque([(box[0],box[1],player[0],player[1],0)]);seen={(box,player)}
        while queue:
            br,bc,pr,pc,pushes=queue.popleft()
            if (br,bc)==target:return pushes
            for dr,dc in ((1,0),(-1,0),(0,1),(0,-1)):
                stand=(br-dr,bc-dc);nbox=(br+dr,bc+dc)
                if not(0<=stand[0]<rows and 0<=stand[1]<cols and 0<=nbox[0]<rows and 0<=nbox[1]<cols)or grid[nbox[0]][nbox[1]]=='#':continue
                walk=deque([(pr,pc)]);reach={(pr,pc)}
                while walk:
                    r,c=walk.popleft()
                    for ar,ac in ((1,0),(-1,0),(0,1),(0,-1)):
                        nr,nc=r+ar,c+ac
                        if 0<=nr<rows and 0<=nc<cols and grid[nr][nc]!='#' and (nr,nc)!=(br,bc) and (nr,nc)not in reach:reach.add((nr,nc));walk.append((nr,nc))
                state=(nbox, (br,bc))
                if stand in reach and state not in seen:seen.add(state);queue.append((nbox[0],nbox[1],br,bc,pushes+1))
        return -1
