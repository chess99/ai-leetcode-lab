# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-11T18:51:28Z
# Experiment: ai-leetcode-lab, round 1
from collections import defaultdict
from typing import List
class Solution:
    def minTime(self, n: int, edges: List[List[int]], hasApple: List[bool]) -> int:
        graph=defaultdict(list)
        for a,b in edges:graph[a].append(b);graph[b].append(a)
        def dfs(node,parent):
            cost=0
            for child in graph[node]:
                if child==parent:continue
                child_cost=dfs(child,node)
                if child_cost or hasApple[child]:cost+=child_cost+2
            return cost
        return dfs(0,-1)
