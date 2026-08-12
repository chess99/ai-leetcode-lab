# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-12T13:47:54Z
# Experiment: ai-leetcode-lab, round 1
from typing import List


class Solution:
    def componentValue(self, nums: List[int], edges: List[List[int]]) -> int:
        size = len(nums)
        if size == 1:
            return 0
        graph = [[] for _ in range(size)]
        for first, second in edges:
            graph[first].append(second)
            graph[second].append(first)
        parent = [-1] * size
        order = [0]
        for node in order:
            for neighbor in graph[node]:
                if neighbor != parent[node]:
                    parent[neighbor] = node
                    order.append(neighbor)

        total = sum(nums)
        maximum = max(nums)
        targets = []
        divisor = 1
        while divisor * divisor <= total:
            if total % divisor == 0:
                targets.append(divisor)
                if divisor * divisor != total:
                    targets.append(total // divisor)
            divisor += 1

        for target in sorted(targets):
            components = total // target
            if target < maximum or components > size:
                continue
            sums = nums[:]
            valid = True
            for node in reversed(order[1:]):
                if sums[node] > target:
                    valid = False
                    break
                if sums[node] < target:
                    sums[parent[node]] += sums[node]
            if valid and sums[0] == target:
                return components - 1
        return 0
