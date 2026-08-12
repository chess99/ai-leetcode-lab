# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-12T16:39:15Z
# Experiment: ai-leetcode-lab, round 1
from typing import List


class Solution:
    def longestCommonPrefix(self, words: List[str], k: int) -> List[int]:
        children = [{}]
        counts = [0]
        depths = [0]
        paths = []
        for word in words:
            node = 0
            path = []
            for char in word:
                next_node = children[node].get(char)
                if next_node is None:
                    next_node = len(children)
                    children[node][char] = next_node
                    children.append({})
                    counts.append(0)
                    depths.append(depths[node] + 1)
                node = next_node
                counts[node] += 1
                path.append(node)
            paths.append(path)

        maximum_depth = max(map(len, words), default=0)
        eligible = [0] * (maximum_depth + 1)
        for node in range(1, len(children)):
            if counts[node] >= k:
                eligible[depths[node]] += 1

        size = 1
        while size <= maximum_depth:
            size *= 2
        tree = [-1] * (size * 2)
        for depth, amount in enumerate(eligible):
            if amount:
                tree[size + depth] = depth
        for node in range(size - 1, 0, -1):
            tree[node] = max(tree[node * 2], tree[node * 2 + 1])

        def adjust(depth: int, delta: int) -> None:
            eligible[depth] += delta
            node = size + depth
            tree[node] = depth if eligible[depth] else -1
            node //= 2
            while node:
                tree[node] = max(tree[node * 2], tree[node * 2 + 1])
                node //= 2

        answer = []
        for path in paths:
            fragile = [node for node in path if counts[node] == k]
            for node in fragile:
                adjust(depths[node], -1)
            answer.append(max(0, tree[1]))
            for node in fragile:
                adjust(depths[node], 1)
        return answer
