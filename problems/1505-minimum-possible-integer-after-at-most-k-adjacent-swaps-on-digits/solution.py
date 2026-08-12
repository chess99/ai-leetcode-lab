# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-12T08:09:58Z
# Experiment: ai-leetcode-lab, round 1
class Solution:
    def minInteger(self, num: str, k: int) -> str:
        from collections import deque
        pos=[deque()for _ in range(10)]
        for i,c in enumerate(num):pos[int(c)].append(i)
        n=len(num);bit=[0]*(n+2)
        def add(i):
            i+=1
            while i<=n:bit[i]+=1;i+=i&-i
        def count(i):
            s=0
            while i:s+=bit[i];i-=i&-i
            return s
        ans=[]
        for _ in range(n):
            for d in range(10):
                if pos[d]:
                    i=pos[d][0];moves=i-count(i)
                    if moves<=k:k-=moves;pos[d].popleft();add(i);ans.append(str(d));break
        return ''.join(ans)
