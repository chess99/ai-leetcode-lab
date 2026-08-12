# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-12T08:09:57Z
# Experiment: ai-leetcode-lab, round 1
from typing import List

class Solution:
    def findCriticalAndPseudoCriticalEdges(self, n: int, edges: List[List[int]]) -> List[List[int]]:
        indexed=[e+[i]for i,e in enumerate(edges)];indexed.sort(key=lambda x:x[2])
        def mst(skip=-1,force=-1):
            p=list(range(n));cost=0;used=0
            def f(x):
                while p[x]!=x:p[x]=p[p[x]];x=p[x]
                return x
            if force>=0:
                a,b,w,_=indexed[force];p[f(a)]=f(b);cost=w;used=1
            for i,(a,b,w,_) in enumerate(indexed):
                if i==skip:continue
                x,y=f(a),f(b)
                if x!=y:p[x]=y;cost+=w;used+=1
            return cost if used==n-1 else 10**9
        base=mst();critical=[];pseudo=[]
        for i,e in enumerate(indexed):
            if mst(i)>base:critical.append(e[3])
            elif mst(-1,i)==base:pseudo.append(e[3])
        return [critical,pseudo]
