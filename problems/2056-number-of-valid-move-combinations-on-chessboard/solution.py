# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-12T12:52:06Z
# Experiment: ai-leetcode-lab, round 1
from typing import List


class Solution:
    def countCombinations(self, pieces: List[str], positions: List[List[int]]) -> int:
        dirs={'rook':[(1,0),(-1,0),(0,1),(0,-1)],'bishop':[(1,1),(1,-1),(-1,1),(-1,-1)],'queen':[(1,0),(-1,0),(0,1),(0,-1),(1,1),(1,-1),(-1,1),(-1,-1)]}
        options=[]
        for p,(x,y) in zip(pieces,positions):
            cur=[(0,0,0)]
            for dx,dy in dirs[p]:
                for d in range(1,8):
                    if 1<=x+dx*d<=8 and 1<=y+dy*d<=8:cur.append((dx,dy,d))
                    else:break
            options.append(cur)
        ans=0
        for moves in __import__('itertools').product(*options):
            good=True
            for t in range(8):
                seen=set()
                for (x,y),(dx,dy,d) in zip(positions,moves):
                    z=min(t,d);pos=(x+dx*z,y+dy*z)
                    if pos in seen:good=False;break
                    seen.add(pos)
                if not good:break
            ans+=good
        return ans
