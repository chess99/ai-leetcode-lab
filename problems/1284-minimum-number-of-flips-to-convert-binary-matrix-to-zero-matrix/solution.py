# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-12T08:09:47Z
# Experiment: ai-leetcode-lab, round 1
from collections import deque
from typing import List

class Solution:
    def minFlips(self, mat: List[List[int]]) -> int:
        rows,columns=len(mat),len(mat[0]);start=sum(mat[r][c]<<(r*columns+c) for r in range(rows) for c in range(columns));masks=[]
        for r in range(rows):
            for c in range(columns):
                mask=0
                for rr,cc in ((r,c),(r-1,c),(r+1,c),(r,c-1),(r,c+1)):
                    if 0<=rr<rows and 0<=cc<columns:mask^=1<<(rr*columns+cc)
                masks.append(mask)
        queue=deque([(start,0)]);seen={start}
        while queue:
            state,moves=queue.popleft()
            if state==0:return moves
            for mask in masks:
                following=state^mask
                if following not in seen:seen.add(following);queue.append((following,moves+1))
        return -1
