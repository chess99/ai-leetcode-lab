# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-12T06:20:11Z
# Experiment: ai-leetcode-lab, round 1
from collections import deque
from typing import List


class Solution:
    def sortItems(self, n: int, m: int, group: List[int], beforeItems: List[List[int]]) -> List[int]:
        group = group[:]
        for item in range(n):
            if group[item] == -1:
                group[item] = m
                m += 1

        item_graph = [[] for _ in range(n)]
        item_indegree = [0] * n
        group_graph = [set() for _ in range(m)]
        group_indegree = [0] * m
        for item, dependencies in enumerate(beforeItems):
            for dependency in dependencies:
                item_graph[dependency].append(item)
                item_indegree[item] += 1
                source, target = group[dependency], group[item]
                if source != target and target not in group_graph[source]:
                    group_graph[source].add(target)
                    group_indegree[target] += 1

        def topological(graph, indegree):
            queue = deque(index for index, degree in enumerate(indegree) if degree == 0)
            order = []
            while queue:
                node = queue.popleft()
                order.append(node)
                for neighbor in graph[node]:
                    indegree[neighbor] -= 1
                    if indegree[neighbor] == 0:
                        queue.append(neighbor)
            return order if len(order) == len(graph) else []

        item_order = topological(item_graph, item_indegree)
        group_order = topological(group_graph, group_indegree)
        if not item_order or not group_order:
            return []
        grouped_items = [[] for _ in range(m)]
        for item in item_order:
            grouped_items[group[item]].append(item)
        return [item for current_group in group_order
                for item in grouped_items[current_group]]
