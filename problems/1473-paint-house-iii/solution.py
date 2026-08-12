# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-12T08:09:56Z
# Experiment: ai-leetcode-lab, round 1
from typing import List

class Solution:
    def minCost(self, houses: List[int], cost: List[List[int]], m: int, n: int, target: int) -> int:
        inf=10**9;dp={(0,0):0}
        for i in range(m):
            nd={}
            for (last,g),v in dp.items():
                for c in range(1,n+1):
                    if houses[i] and houses[i]!=c:continue
                    key=(c,g+(c!=last));nd[key]=min(nd.get(key,inf),v+(0 if houses[i] else cost[i][c-1]))
            dp=nd
        ans=min((v for (c,g),v in dp.items() if g==target),default=inf);return -1 if ans==inf else ans
