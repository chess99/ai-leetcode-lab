# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-12T16:38:23Z
# Experiment: ai-leetcode-lab, round 1
from typing import List


class Solution:
    def maxStability(self, n: int, edges: List[List[int]], k: int) -> int:
        values=sorted({s for _,_,s,_ in edges}|{2*s for _,_,s,m in edges if not m})
        def ok(x):
            p=list(range(n))
            def f(a):
                while p[a]!=a:p[a]=p[p[a]];a=p[a]
                return a
            used=0
            for a,b,s,m in edges:
                if m:
                    if s<x:return False
                    a,b=f(a),f(b)
                    if a==b:return False
                    p[a]=b
            opts=[]
            for a,b,s,m in edges:
                if not m and 2*s>=x:opts.append((s<x,a,b))
            opts.sort()
            for upgrade,a,b in opts:
                a,b=f(a),f(b)
                if a!=b:p[a]=b;used+=upgrade
            return used<=k and len({f(i) for i in range(n)})==1
        lo,hi=0,len(values)-1;ans=-1
        while lo<=hi:
            mid=(lo+hi)//2
            if ok(values[mid]):ans=values[mid];lo=mid+1
            else:hi=mid-1
        return ans
