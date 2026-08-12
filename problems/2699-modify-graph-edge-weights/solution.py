# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-12T14:40:38Z
# Experiment: ai-leetcode-lab, round 1
from typing import List
class Solution:
    def modifiedGraphEdges(self, n: int, edges: List[List[int]], source: int, destination: int, target: int) -> List[List[int]]:
        import heapq
        graph=[[] for _ in range(n)]
        for i,(a,b,_) in enumerate(edges):graph[a].append((b,i));graph[b].append((a,i))
        def dijkstra(start, unknown_one=True):
            dist=[10**18]*n;dist[start]=0;heap=[(0,start)]
            while heap:
                d,u=heapq.heappop(heap)
                if d!=dist[u]:continue
                for v,i in graph[u]:
                    w=edges[i][2]
                    if w<0:w=1 if unknown_one else 10**9
                    if d+w<dist[v]:dist[v]=d+w;heapq.heappush(heap,(d+w,v))
            return dist
        to_dest=dijkstra(destination)
        if to_dest[source]>target:return []
        dist=[10**18]*n;dist[source]=0;heap=[(0,source)]
        while heap:
            d,u=heapq.heappop(heap)
            if d!=dist[u]:continue
            for v,i in graph[u]:
                if edges[i][2]<0:
                    edges[i][2]=max(1,target-d-to_dest[v])
                w=edges[i][2]
                if d+w<dist[v]:dist[v]=d+w;heapq.heappush(heap,(d+w,v))
        if dist[destination]!=target:return []
        for e in edges:
            if e[2]<0:e[2]=10**9
        return edges
