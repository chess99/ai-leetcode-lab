# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-12T11:06:31Z
# Experiment: ai-leetcode-lab, round 1
from typing import List
class Solution:
    def maxNumEdgesToRemove(self, n: int, edges: List[List[int]]) -> int:
        class DSU:
            def __init__(self):self.parent=list(range(n+1));self.components=n
            def find(self,x):
                while self.parent[x]!=x:self.parent[x]=self.parent[self.parent[x]];x=self.parent[x]
                return x
            def union(self,a,b):
                a,b=self.find(a),self.find(b)
                if a==b:return False
                self.parent[a]=b;self.components-=1;return True
        alice,bob=DSU(),DSU();used=0
        for kind,a,b in edges:
            if kind==3:
                merged=alice.union(a,b);bob.union(a,b);used+=merged
        for kind,a,b in edges:
            if kind==1:used+=alice.union(a,b)
            elif kind==2:used+=bob.union(a,b)
        return len(edges)-used if alice.components==bob.components==1 else -1
