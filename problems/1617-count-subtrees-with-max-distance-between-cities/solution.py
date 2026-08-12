# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-12T11:06:34Z
# Experiment: ai-leetcode-lab, round 1
from collections import deque
from typing import List
class Solution:
    def countSubgraphsForEachDiameter(self, n: int, edges: List[List[int]]) -> List[int]:
        graph=[[] for _ in range(n)]
        for a,b in edges:a-=1;b-=1;graph[a].append(b);graph[b].append(a)
        answer=[0]*(n-1)
        for mask in range(1,1<<n):
            start=(mask&-mask).bit_length()-1;queue=deque([(start,0)]);seen={start};farthest=(start,0)
            while queue:
                node,distance=queue.popleft();farthest=max(farthest,(node,distance),key=lambda x:x[1])
                for following in graph[node]:
                    if mask>>following&1 and following not in seen:seen.add(following);queue.append((following,distance+1))
            if len(seen)!=mask.bit_count():continue
            queue=deque([(farthest[0],0)]);seen={farthest[0]};diameter=0
            while queue:
                node,distance=queue.popleft();diameter=max(diameter,distance)
                for following in graph[node]:
                    if mask>>following&1 and following not in seen:seen.add(following);queue.append((following,distance+1))
            if diameter:answer[diameter-1]+=1
        return answer
