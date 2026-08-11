# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-11T18:55:38Z
# Experiment: ai-leetcode-lab, round 1
from collections import defaultdict
from typing import List
class Solution:
    def countSubTrees(self, n: int, edges: List[List[int]], labels: str) -> List[int]:
        graph=defaultdict(list)
        for a,b in edges:graph[a].append(b);graph[b].append(a)
        answer=[0]*n
        def dfs(node,parent):
            counts=[0]*26
            for child in graph[node]:
                if child!=parent:
                    child_counts=dfs(child,node)
                    for i in range(26):counts[i]+=child_counts[i]
            index=ord(labels[node])-97;counts[index]+=1;answer[node]=counts[index]
            return counts
        dfs(0,-1);return answer
