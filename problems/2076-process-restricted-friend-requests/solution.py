# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-12T12:52:07Z
# Experiment: ai-leetcode-lab, round 1
from typing import List


class Solution:
    def friendRequests(self, n: int, restrictions: List[List[int]], requests: List[List[int]]) -> List[bool]:
        parent=list(range(n))
        def find(x):
            while parent[x]!=x:parent[x]=parent[parent[x]];x=parent[x]
            return x
        ans=[]
        for a,b in requests:
            x,y=find(a),find(b); good=True
            if x!=y:
                for u,v in restrictions:
                    if {find(u),find(v)}=={x,y}:good=False;break
            ans.append(good)
            if good and x!=y:parent[x]=y
        return ans
