# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-11T18:55:38Z
# Experiment: ai-leetcode-lab, round 1
import heapq
from collections import defaultdict
from typing import List
class Solution:
    def maxProbability(self, n: int, edges: List[List[int]], succProb: List[float], start_node: int, end_node: int) -> float:
        graph=defaultdict(list)
        for (a,b),p in zip(edges,succProb):graph[a].append((b,p));graph[b].append((a,p))
        best=[0.0]*n;best[start_node]=1;heap=[(-1.0,start_node)]
        while heap:
            probability,node=heapq.heappop(heap);probability=-probability
            if node==end_node:return probability
            if probability<best[node]:continue
            for nxt,p in graph[node]:
                value=probability*p
                if value>best[nxt]:best[nxt]=value;heapq.heappush(heap,(-value,nxt))
        return 0.0
