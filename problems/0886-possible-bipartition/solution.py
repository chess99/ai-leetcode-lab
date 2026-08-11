# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-11T17:56:15Z
# Experiment: ai-leetcode-lab, round 1
from collections import deque
from typing import List
class Solution:
    def possibleBipartition(self, n: int, dislikes: List[List[int]]) -> bool:
        graph=[[] for _ in range(n)]
        for a,b in dislikes: graph[a-1].append(b-1);graph[b-1].append(a-1)
        color=[0]*n
        for start in range(n):
            if color[start]: continue
            color[start]=1; queue=deque([start])
            while queue:
                node=queue.popleft()
                for nxt in graph[node]:
                    if color[nxt]==color[node]: return False
                    if not color[nxt]: color[nxt]=-color[node];queue.append(nxt)
        return True
