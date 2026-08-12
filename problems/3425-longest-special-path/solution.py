# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-12T16:38:07Z
# Experiment: ai-leetcode-lab, round 1
import sys
from typing import List


class Solution:
    def longestSpecialPath(self, edges: List[List[int]], nums: List[int]) -> List[int]:
        sys.setrecursionlimit(200_000)
        n = len(nums)
        graph = [[] for _ in range(n)]
        for u, v, weight in edges:
            graph[u].append((v, weight))
            graph[v].append((u, weight))

        last_depth = {}
        path_distance = []
        best_length = 0
        best_nodes = 1

        def dfs(node: int, parent: int, distance: int, left: int) -> None:
            nonlocal best_length, best_nodes
            depth = len(path_distance)
            path_distance.append(distance)
            previous = last_depth.get(nums[node], -1)
            new_left = max(left, previous + 1)
            last_depth[nums[node]] = depth

            length = distance - path_distance[new_left]
            nodes = depth - new_left + 1
            if length > best_length or (length == best_length and nodes < best_nodes):
                best_length, best_nodes = length, nodes

            for neighbor, weight in graph[node]:
                if neighbor != parent:
                    dfs(neighbor, node, distance + weight, new_left)

            if previous < 0:
                del last_depth[nums[node]]
            else:
                last_depth[nums[node]] = previous
            path_distance.pop()

        dfs(0, -1, 0, 0)
        return [best_length, best_nodes]
