# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-12T11:06:32Z
# Experiment: ai-leetcode-lab, round 1
from typing import List
class Solution:
    def connectTwoGroups(self, cost: List[List[int]]) -> int:
        m,n=len(cost),len(cost[0]);dp={0:0}
        for row in cost:
            following={}
            for mask,value in dp.items():
                for column,edge in enumerate(row):
                    new=mask|1<<column;following[new]=min(following.get(new,10**9),value+edge)
            dp=following
        minimum=[min(cost[r][c] for r in range(m)) for c in range(n)];return min(value+sum(minimum[c] for c in range(n) if not mask>>c&1) for mask,value in dp.items())
