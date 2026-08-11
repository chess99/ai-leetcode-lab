# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-11T19:34:26Z
# Experiment: ai-leetcode-lab, round 1
from collections import defaultdict
from typing import List
class Solution:
    def restoreArray(self, adjacentPairs: List[List[int]]) -> List[int]:
        graph=defaultdict(list)
        for a,b in adjacentPairs:graph[a].append(b);graph[b].append(a)
        result=[next(x for x in graph if len(graph[x])==1)]
        while len(result)<len(graph):result.append(next(x for x in graph[result[-1]] if len(result)<2 or x!=result[-2]))
        return result
