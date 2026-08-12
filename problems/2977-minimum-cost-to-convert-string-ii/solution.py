# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-12T15:15:51Z
# Experiment: ai-leetcode-lab, round 1
from typing import List
class Solution:
    def minimumCost(self, source: str, target: str, original: List[str], changed: List[str], cost: List[int]) -> int:
        words=set(original+changed);ids={w:i for i,w in enumerate(words)};n=len(ids);inf=10**18
        d=[[inf]*n for _ in range(n)]
        for i in range(n):d[i][i]=0
        for a,b,c in zip(original,changed,cost):d[ids[a]][ids[b]]=min(d[ids[a]][ids[b]],c)
        for z in range(n):
            for i in range(n):
                for j in range(n):d[i][j]=min(d[i][j],d[i][z]+d[z][j])
        lens=set(map(len,words));dp=[inf]*(len(source)+1);dp[0]=0
        for i in range(len(source)):
            if source[i]==target[i]:dp[i+1]=min(dp[i+1],dp[i])
            for l in lens:
                a=source[i:i+l];b=target[i:i+l]
                if len(a)==l and a in ids and b in ids:dp[i+l]=min(dp[i+l],dp[i]+d[ids[a]][ids[b]])
        return -1 if dp[-1]>=inf else dp[-1]
