# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-12T15:57:32Z
# Experiment: ai-leetcode-lab, round 1
from typing import List


class Solution:
    def shortestDistanceAfterQueries(self, n: int, queries: List[List[int]]) -> List[int]:
        successor = list(range(n + 1))

        def find(node: int) -> int:
            root = node
            while successor[root] != root:
                root = successor[root]
            while successor[node] != node:
                next_node = successor[node]
                successor[node] = root
                node = next_node
            return root

        distance = n - 1
        answer = []
        for start, end in queries:
            city = find(start + 1)
            while city < end:
                successor[city] = find(city + 1)
                distance -= 1
                city = find(city)
            answer.append(distance)
        return answer
