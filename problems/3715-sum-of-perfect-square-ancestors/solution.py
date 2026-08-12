# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-12T17:28:49Z
# Experiment: ai-leetcode-lab, round 1
from typing import List


class Solution:
    def sumOfAncestors(self, n: int, edges: List[List[int]], nums: List[int]) -> int:
        calpenodra = (n, edges, nums)
        graph = [[] for _ in range(n)]
        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)

        maximum = max(nums)
        spf = list(range(maximum + 1))
        for value in range(2, int(maximum ** 0.5) + 1):
            if spf[value] != value:
                continue
            for multiple in range(value * value, maximum + 1, value):
                if spf[multiple] == multiple:
                    spf[multiple] = value

        def square_free_kernel(value: int) -> int:
            kernel = 1
            while value > 1:
                prime = spf[value]
                parity = 0
                while value % prime == 0:
                    value //= prime
                    parity ^= 1
                if parity:
                    kernel *= prime
            return kernel

        kernels = [square_free_kernel(value) for value in nums]
        path_count = {}
        answer = 0
        stack = [(0, -1, False)]
        while stack:
            node, parent, leaving = stack.pop()
            kernel = kernels[node]
            if leaving:
                path_count[kernel] -= 1
                continue

            answer += path_count.get(kernel, 0)
            path_count[kernel] = path_count.get(kernel, 0) + 1
            stack.append((node, parent, True))
            for child in graph[node]:
                if child != parent:
                    stack.append((child, node, False))

        return answer
