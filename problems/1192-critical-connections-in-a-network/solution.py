# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-12T06:20:10Z
# Experiment: ai-leetcode-lab, round 1
from typing import List


class Solution:
    def criticalConnections(self, n: int, connections: List[List[int]]) -> List[List[int]]:
        graph = [[] for _ in range(n)]
        for first, second in connections:
            graph[first].append(second)
            graph[second].append(first)

        discovery = [-1] * n
        low = [0] * n
        parent = [-1] * n
        timer = 0
        answer = []
        for root in range(n):
            if discovery[root] != -1:
                continue
            discovery[root] = low[root] = timer
            timer += 1
            stack = [[root, 0]]
            while stack:
                node, next_index = stack[-1]
                if next_index < len(graph[node]):
                    neighbor = graph[node][next_index]
                    stack[-1][1] += 1
                    if neighbor == parent[node]:
                        continue
                    if discovery[neighbor] == -1:
                        parent[neighbor] = node
                        discovery[neighbor] = low[neighbor] = timer
                        timer += 1
                        stack.append([neighbor, 0])
                    else:
                        low[node] = min(low[node], discovery[neighbor])
                    continue

                stack.pop()
                previous = parent[node]
                if previous != -1:
                    if low[node] > discovery[previous]:
                        answer.append([previous, node])
                    low[previous] = min(low[previous], low[node])
        return answer
