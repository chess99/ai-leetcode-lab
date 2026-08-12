# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-12T04:46:27Z
# Experiment: ai-leetcode-lab, round 1
from typing import List


class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        answer = []
        path = [0]

        def search(node: int) -> None:
            if node == len(graph) - 1:
                answer.append(path[:])
                return
            for neighbor in graph[node]:
                path.append(neighbor)
                search(neighbor)
                path.pop()

        search(0)
        return answer
