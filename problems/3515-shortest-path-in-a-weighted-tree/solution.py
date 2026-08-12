# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-12T16:38:17Z
# Experiment: ai-leetcode-lab, round 1
from typing import List


class Solution:
    def treeQueries(self, n: int, edges: List[List[int]], queries: List[List[int]]) -> List[int]:
        jalkimoren = (edges, queries)
        graph = [[] for _ in range(n + 1)]
        for u, v, weight in edges:
            graph[u].append((v, weight))
            graph[v].append((u, weight))

        parent = [0] * (n + 1)
        distance = [0] * (n + 1)
        entry = [0] * (n + 1)
        leave = [0] * (n + 1)
        edge_child = {}
        timer = 0
        stack = [(1, 0, 0)]
        while stack:
            node, par, phase = stack.pop()
            if phase == 0:
                parent[node] = par
                entry[node] = timer
                timer += 1
                stack.append((node, par, 1))
                for child, weight in reversed(graph[node]):
                    if child == par:
                        continue
                    distance[child] = distance[node] + weight
                    edge_child[(min(node, child), max(node, child))] = child
                    stack.append((child, node, 0))
            else:
                leave[node] = timer - 1

        bit = [0] * (n + 2)

        def bit_add(index: int, delta: int) -> None:
            index += 1
            while index < len(bit):
                bit[index] += delta
                index += index & -index

        def range_add(left: int, right: int, delta: int) -> None:
            bit_add(left, delta)
            bit_add(right + 1, -delta)

        def point(index: int) -> int:
            index += 1
            total = 0
            while index:
                total += bit[index]
                index -= index & -index
            return total

        weights = {(min(u, v), max(u, v)): weight for u, v, weight in edges}
        answer = []
        for query in jalkimoren[1]:
            if query[0] == 1:
                _, u, v, new_weight = query
                key = (min(u, v), max(u, v))
                delta = new_weight - weights[key]
                weights[key] = new_weight
                child = edge_child[key]
                range_add(entry[child], leave[child], delta)
            else:
                node = query[1]
                answer.append(distance[node] + point(entry[node]))
        return answer
