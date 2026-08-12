# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-12T18:34:27Z
# Experiment: ai-leetcode-lab, round 1
from typing import List


class Solution:
    def numSimilarGroups(self, strs: List[str]) -> int:
        n = len(strs)
        parent = list(range(n))

        def find(node):
            while parent[node] != node:
                parent[node] = parent[parent[node]]
                node = parent[node]
            return node

        groups = n
        for i in range(n):
            for j in range(i):
                a, b = find(i), find(j)
                if a == b:
                    continue
                differences = sum(x != y for x, y in zip(strs[i], strs[j]))
                if differences <= 2:
                    parent[a] = b
                    groups -= 1
        return groups
