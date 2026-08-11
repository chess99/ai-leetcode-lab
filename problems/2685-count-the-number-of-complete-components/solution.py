# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-11T21:14:12Z
# Experiment: ai-leetcode-lab, round 1
from typing import List
class Solution:
    def countCompleteComponents(self, n: int, edges: List[List[int]]) -> int:
        graph=[[] for _ in range(n)]
        for a,b in edges: graph[a].append(b); graph[b].append(a)
        seen=set(); answer=0
        for start in range(n):
            if start in seen: continue
            stack=[start]; seen.add(start); nodes=edges_count=0
            while stack:
                node=stack.pop(); nodes+=1; edges_count+=len(graph[node])
                for nxt in graph[node]:
                    if nxt not in seen: seen.add(nxt); stack.append(nxt)
            if edges_count==nodes*(nodes-1): answer+=1
        return answer
