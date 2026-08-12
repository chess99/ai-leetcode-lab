# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-12T16:38:20Z
# Experiment: ai-leetcode-lab, round 1
from typing import List


class Solution:
    def maxProfit(self, n: int, present: List[int], future: List[int], hierarchy: List[List[int]], budget: int) -> int:
        g=[[] for _ in range(n)]
        for a,b in hierarchy:g[a-1].append(b-1)
        def dfs(u):
            # dp[parent did not buy], dp[parent bought]; each entry maps cost to profit.
            child_states=[dfs(v) for v in g[u]]
            result=[]
            for discounted in (False, True):
                dp0=[0]+[-10**9]*budget
                dp1=[-10**9]*(budget+1)
                price=present[u]//2 if discounted else present[u]
                if price<=budget:dp1[price]=future[u]-price
                for child in child_states:
                    nd0=[-10**9]*(budget+1);nd1=[-10**9]*(budget+1)
                    for a in range(budget+1):
                        for b in range(budget-a+1):
                            nd0[a+b]=max(nd0[a+b],dp0[a]+child[0][b])
                            nd1[a+b]=max(nd1[a+b],dp1[a]+child[1][b])
                    dp0,dp1=nd0,nd1
                result.append([max(dp0[i],dp1[i]) for i in range(budget+1)])
            return result
        return max(dfs(0)[0])
