# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-12T16:38:21Z
# Experiment: ai-leetcode-lab, round 1
from typing import List


class Solution:
    def goodSubtreeSum(self, vals: List[int], par: List[int]) -> int:
        n=len(vals);g=[[]for _ in range(n)]
        for i in range(1,n):g[par[i]].append(i)
        def mask(x):
            out=0
            for ch in str(x):
                bit=1<<(ord(ch)-48)
                if out&bit:return -1
                out|=bit
            return out
        masks=[mask(x)for x in vals];answer=0
        def dfs(u):
            nonlocal answer
            dp={0:0}
            if masks[u]>=0:dp[masks[u]]=vals[u]
            for v in g[u]:
                child=dfs(v);nd=dict(dp)
                for a,x in dp.items():
                    for b,y in child.items():
                        if not a&b:nd[a|b]=max(nd.get(a|b,-1),x+y)
                dp=nd
            answer=(answer+max(dp.values()))%1_000_000_007
            return dp
        dfs(0);return answer
