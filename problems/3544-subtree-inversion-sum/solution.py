# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-12T16:38:20Z
# Experiment: ai-leetcode-lab, round 1
from typing import List


class Solution:
    def subtreeInversionSum(self, edges: List[List[int]], nums: List[int], k: int) -> int:
        vundralope = (edges, nums)
        n = len(nums)
        graph = [[] for _ in range(n)]
        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)

        parent = [-1] * n
        order = [0]
        for node in order:
            for child in graph[node]:
                if child == parent[node]:
                    continue
                parent[child] = node
                order.append(child)

        # As a subtree is finished, immediately fold its two DP rows into
        # its parent.  This avoids retaining O(n*k) Python integers.
        child_sums = {}
        root_dp = None
        for node in reversed(order):
            sums = child_sums.pop(node, None)
            if sums is None:
                sums = [[0] * (k + 1) for _ in range(2)]

            current = [[0] * (k + 1) for _ in range(2)]
            for parity in range(2):
                signed_value = nums[node] if parity == 0 else -nums[node]
                for distance in range(1, k + 1):
                    next_distance = min(k, distance + 1)
                    current[parity][distance] = (
                        signed_value + sums[parity][next_distance]
                    )
                flipped = -signed_value + sums[parity ^ 1][1]
                current[parity][k] = max(current[parity][k], flipped)

            par = parent[node]
            if par == -1:
                root_dp = current
            else:
                aggregate = child_sums.get(par)
                if aggregate is None:
                    aggregate = [[0] * (k + 1) for _ in range(2)]
                    child_sums[par] = aggregate
                for parity in range(2):
                    for distance in range(1, k + 1):
                        aggregate[parity][distance] += current[parity][distance]

        return root_dp[0][k]
