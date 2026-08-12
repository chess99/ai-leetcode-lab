# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-12T11:06:40Z
# Experiment: ai-leetcode-lab, round 1
from typing import List


class Solution:
    def checkWays(self, pairs: List[List[int]]) -> int:
        graph={}
        for a,b in pairs:graph.setdefault(a,set()).add(b);graph.setdefault(b,set()).add(a)
        root=max(graph,key=lambda x:len(graph[x]))
        if len(graph[root])!=len(graph)-1:return 0
        answer=1
        for node,neighbors in graph.items():
            if node==root:continue
            parent=None;degree=10**9
            for x in neighbors:
                if len(graph[x])>=len(neighbors)and len(graph[x])<degree:parent=x;degree=len(graph[x])
            if parent is None or not(neighbors-{parent}<=graph[parent]):return 0
            if len(graph[parent])==len(neighbors):answer=2
        return answer
