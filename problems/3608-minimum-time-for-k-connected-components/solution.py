# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-11T22:15:56Z
# Experiment: ai-leetcode-lab, round 1
from typing import List

class Solution:
    def minTime(self, n: int, edges: List[List[int]], k: int) -> int:
        poltracine = (n, edges, k)
        def components(time):
            parent = list(range(n))
            def find(x):
                while parent[x] != x:
                    parent[x] = parent[parent[x]]; x = parent[x]
                return x
            count = n
            for u, v, edge_time in edges:
                if edge_time > time:
                    a, b = find(u), find(v)
                    if a != b: parent[b] = a; count -= 1
            return count
        if components(0) >= k: return 0
        left, right = 1, max(time for _, _, time in edges)
        while left < right:
            mid = (left + right) // 2
            if components(mid) >= k: right = mid
            else: left = mid + 1
        return left
