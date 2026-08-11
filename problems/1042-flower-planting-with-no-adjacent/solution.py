# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-11T18:13:28Z
# Experiment: ai-leetcode-lab, round 1
from typing import List
class Solution:
    def gardenNoAdj(self, n: int, paths: List[List[int]]) -> List[int]:
        graph=[[] for _ in range(n)];colors=[0]*n
        for a,b in paths:graph[a-1].append(b-1);graph[b-1].append(a-1)
        for garden in range(n): colors[garden]=next(color for color in range(1,5) if color not in {colors[x] for x in graph[garden]})
        return colors
