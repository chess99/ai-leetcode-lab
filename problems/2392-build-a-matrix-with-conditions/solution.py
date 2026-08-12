# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-12T13:47:51Z
# Experiment: ai-leetcode-lab, round 1
import heapq
from typing import List


class Solution:
    def buildMatrix(self, k: int, rowConditions: List[List[int]], colConditions: List[List[int]]) -> List[List[int]]:
        def order(conditions):
            graph = [[] for _ in range(k)]
            indegree = [0] * k
            for before, after in conditions:
                graph[before - 1].append(after - 1)
                indegree[after - 1] += 1
            queue = [node for node, degree in enumerate(indegree) if degree == 0]
            heapq.heapify(queue)
            result = []
            while queue:
                node = heapq.heappop(queue)
                result.append(node)
                for neighbor in graph[node]:
                    indegree[neighbor] -= 1
                    if indegree[neighbor] == 0:
                        heapq.heappush(queue, neighbor)
            return result if len(result) == k else []

        rows = order(rowConditions)
        columns = order(colConditions)
        if not rows or not columns:
            return []
        row_position = [0] * k
        column_position = [0] * k
        for index, value in enumerate(rows):
            row_position[value] = index
        for index, value in enumerate(columns):
            column_position[value] = index
        matrix = [[0] * k for _ in range(k)]
        for value in range(k):
            matrix[row_position[value]][column_position[value]] = value + 1
        return matrix
