# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-11T16:45:56Z
# Experiment: ai-leetcode-lab, round 1
from typing import List
class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        if n == 1: return [0]
        graph = [set() for _ in range(n)]
        for first, second in edges: graph[first].add(second); graph[second].add(first)
        leaves = [node for node in range(n) if len(graph[node]) == 1]
        while n > 2:
            n -= len(leaves); next_leaves = []
            for leaf in leaves:
                neighbor = graph[leaf].pop(); graph[neighbor].remove(leaf)
                if len(graph[neighbor]) == 1: next_leaves.append(neighbor)
            leaves = next_leaves
        return leaves
