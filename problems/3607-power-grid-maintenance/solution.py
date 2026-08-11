# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-11T22:15:56Z
# Experiment: ai-leetcode-lab, round 1
from typing import List
import heapq

class Solution:
    def processQueries(self, c: int, connections: List[List[int]], queries: List[List[int]]) -> List[int]:
        parent = list(range(c + 1))
        def find(x):
            while parent[x] != x:
                parent[x] = parent[parent[x]]; x = parent[x]
            return x
        def union(a, b):
            a, b = find(a), find(b)
            if a != b: parent[b] = a
        for a, b in connections: union(a, b)
        heaps = {}
        for x in range(1, c + 1): heaps.setdefault(find(x), []).append(x)
        for heap in heaps.values(): heapq.heapify(heap)
        online = [True] * (c + 1)
        ans = []
        for kind, x in queries:
            if kind == 2: online[x] = False
            elif online[x]: ans.append(x)
            else:
                heap = heaps[find(x)]
                while heap and not online[heap[0]]: heapq.heappop(heap)
                ans.append(heap[0] if heap else -1)
        return ans
