# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-12T13:47:44Z
# Experiment: ai-leetcode-lab, round 1
from typing import List


class Solution:
    def longestPath(self, parent: List[int], s: str) -> int:
        size = len(parent)
        children = [[] for _ in range(size)]
        for node in range(1, size):
            children[parent[node]].append(node)

        order = [0]
        for node in order:
            order.extend(children[node])

        longest_down = [1] * size
        answer = 1
        for node in reversed(order):
            first = second = 0
            for child in children[node]:
                if s[child] == s[node]:
                    continue
                length = longest_down[child]
                if length > first:
                    second = first
                    first = length
                elif length > second:
                    second = length
            longest_down[node] = first + 1
            answer = max(answer, first + second + 1)
        return answer
