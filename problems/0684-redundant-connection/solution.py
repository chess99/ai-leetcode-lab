# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-11T17:31:04Z
# Experiment: ai-leetcode-lab, round 1
from typing import List


class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        parent = list(range(len(edges) + 1))
        def find(x):
            while x != parent[x]: parent[x] = parent[parent[x]]; x = parent[x]
            return x
        for a, b in edges:
            root_a, root_b = find(a), find(b)
            if root_a == root_b: return [a, b]
            parent[root_a] = root_b
