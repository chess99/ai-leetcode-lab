# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-11T20:37:20Z
# Experiment: ai-leetcode-lab, round 1
from typing import List


class Solution:
    def mostProfitablePath(self, edges: List[List[int]], bob: int, amount: List[int]) -> int:
        nodes = len(amount)
        graph = [[] for _ in range(nodes)]
        for first, second in edges:
            graph[first].append(second)
            graph[second].append(first)

        parent = [-1] * nodes
        stack = [0]
        while stack:
            node = stack.pop()
            for neighbor in graph[node]:
                if neighbor == parent[node]:
                    continue
                parent[neighbor] = node
                stack.append(neighbor)

        bob_time = [nodes] * nodes
        node = bob
        time = 0
        while True:
            bob_time[node] = time
            if node == 0:
                break
            node = parent[node]
            time += 1

        best_score = -10**18
        alice_stack = [(0, -1, 0, 0)]

        while alice_stack:
            node, previous, time, score = alice_stack.pop()

            if time < bob_time[node]:
                score += amount[node]
            elif time == bob_time[node]:
                score += amount[node] // 2

            if node != 0 and len(graph[node]) == 1:
                best_score = max(best_score, score)
                continue

            for neighbor in graph[node]:
                if neighbor != previous:
                    alice_stack.append((neighbor, node, time + 1, score))

        return best_score
