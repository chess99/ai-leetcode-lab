# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-11T21:59:15Z
# Experiment: ai-leetcode-lab, round 1
from typing import List


class Solution:
    def findSubtreeSizes(self, parent: List[int], s: str) -> List[int]:
        n = len(parent)
        children = [[] for _ in range(n)]
        for node in range(1, n):
            children[parent[node]].append(node)
        changed = parent[:]
        path = [[] for _ in range(26)]

        stack = [(0, False)]
        while stack:
            node, leaving = stack.pop()
            bucket = path[ord(s[node]) - 97]
            if leaving:
                bucket.pop()
                continue
            if bucket:
                changed[node] = bucket[-1]
            bucket.append(node)
            stack.append((node, True))
            stack.extend((child, False) for child in children[node])

        final_children = [[] for _ in range(n)]
        for node in range(1, n):
            final_children[changed[node]].append(node)
        result = [1] * n
        order = [0]
        for node in order:
            order.extend(final_children[node])
        for node in reversed(order[1:]):
            result[changed[node]] += result[node]
        return result
