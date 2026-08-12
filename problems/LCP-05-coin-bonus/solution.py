# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-12T17:58:43Z
# Experiment: ai-leetcode-lab, round 1
from typing import List


class Solution:
    def bonus(self, n: int, leadership: List[List[int]], operations: List[List[int]]) -> List[int]:
        graph = [[] for _ in range(n + 1)]
        for leader, member in leadership:
            graph[leader].append(member)
        start = [0] * (n + 1)
        end = [0] * (n + 1)
        timer = 0
        stack = [(1, False)]
        while stack:
            node, leaving = stack.pop()
            if leaving:
                end[node] = timer - 1
                continue
            start[node] = timer
            timer += 1
            stack.append((node, True))
            for child in reversed(graph[node]):
                stack.append((child, False))

        bit1 = [0] * (n + 2)
        bit2 = [0] * (n + 2)

        def add(bit, index, delta):
            index += 1
            while index < len(bit):
                bit[index] += delta
                index += index & -index

        def range_add(left, right, delta):
            add(bit1, left, delta)
            add(bit1, right + 1, -delta)
            add(bit2, left, delta * left)
            add(bit2, right + 1, -delta * (right + 1))

        def prefix(index):
            result1 = result2 = 0
            original = index + 1
            index += 1
            while index:
                result1 += bit1[index]
                result2 += bit2[index]
                index -= index & -index
            return result1 * original - result2

        mod = 1_000_000_007
        answer = []
        for operation in operations:
            kind, node = operation[:2]
            if kind == 1:
                range_add(start[node], start[node], operation[2])
            elif kind == 2:
                range_add(start[node], end[node], operation[2])
            else:
                answer.append((prefix(end[node]) - prefix(start[node] - 1)) % mod)
        return answer
