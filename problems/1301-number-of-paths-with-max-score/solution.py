# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-12T08:09:48Z
# Experiment: ai-leetcode-lab, round 1
from typing import List
class Solution:
    def pathsWithMaxScore(self, board: List[str]) -> List[int]:
        n=len(board);mod=1_000_000_007;score=[[-1]*n for _ in range(n)];ways=[[0]*n for _ in range(n)];score[-1][-1]=0;ways[-1][-1]=1
        for r in range(n-1,-1,-1):
            for c in range(n-1,-1,-1):
                if board[r][c]=='X' or (r==n-1 and c==n-1):continue
                previous=[(score[rr][cc],ways[rr][cc]) for rr,cc in ((r+1,c),(r,c+1),(r+1,c+1)) if rr<n and cc<n and score[rr][cc]>=0]
                if not previous:continue
                best=max(x for x,w in previous);score[r][c]=best+(int(board[r][c]) if board[r][c].isdigit() else 0);ways[r][c]=sum(w for x,w in previous if x==best)%mod
        return [max(0,score[0][0]),ways[0][0]]
