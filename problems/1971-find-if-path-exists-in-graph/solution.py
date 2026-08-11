# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-11T12:52:50Z
# Experiment: ai-leetcode-lab, round 1
class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        graph=[[] for _ in range(n)]
        for a,b in edges:graph[a].append(b);graph[b].append(a)
        seen={source};stack=[source]
        while stack:
            node=stack.pop()
            if node==destination:return True
            for neighbor in graph[node]:
                if neighbor not in seen:seen.add(neighbor);stack.append(neighbor)
        return False
