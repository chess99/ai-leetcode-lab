# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-12T12:52:08Z
# Experiment: ai-leetcode-lab, round 1
from collections import defaultdict
from typing import List


class Solution:
    def validArrangement(self, pairs: List[List[int]]) -> List[List[int]]:
        graph = defaultdict(list)
        degree = defaultdict(int)
        for start, end in pairs:
            graph[start].append(end)
            degree[start] += 1
            degree[end] -= 1
        start = next((node for node, value in degree.items() if value == 1), pairs[0][0])
        stack = [start]
        path = []
        while stack:
            if graph[stack[-1]]:
                stack.append(graph[stack[-1]].pop())
            else:
                path.append(stack.pop())
        path.reverse()
        return [[path[index], path[index + 1]] for index in range(len(pairs))]
