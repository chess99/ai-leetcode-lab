# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-12T06:02:54Z
# Experiment: ai-leetcode-lab, round 1
from collections import deque
from typing import List


class Solution:
    def shortestPathLength(self, graph: List[List[int]]) -> int:
        n=len(graph);target=(1<<n)-1;queue=deque((i,1<<i,0) for i in range(n));seen={(i,1<<i) for i in range(n)}
        while queue:
            node,mask,distance=queue.popleft()
            if mask==target:return distance
            for neighbor in graph[node]:
                state=(neighbor,mask|1<<neighbor)
                if state not in seen:seen.add(state);queue.append((state[0],state[1],distance+1))
