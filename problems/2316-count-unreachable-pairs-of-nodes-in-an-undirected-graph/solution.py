# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-11T20:21:26Z
# Experiment: ai-leetcode-lab, round 1
from typing import List


class Solution:
    def countPairs(self, n: int, edges: List[List[int]]) -> int:
        parent = list(range(n))
        sizes = [1] * n

        def find(node: int) -> int:
            while node != parent[node]:
                parent[node] = parent[parent[node]]
                node = parent[node]
            return node

        for first, second in edges:
            first_root = find(first)
            second_root = find(second)
            if first_root == second_root:
                continue

            if sizes[first_root] < sizes[second_root]:
                first_root, second_root = second_root, first_root
            parent[second_root] = first_root
            sizes[first_root] += sizes[second_root]

        unreachable_pairs = 0
        processed_nodes = 0

        for node in range(n):
            if parent[node] == node:
                unreachable_pairs += sizes[node] * processed_nodes
                processed_nodes += sizes[node]

        return unreachable_pairs
