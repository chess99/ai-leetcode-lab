# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-11T20:37:23Z
# Experiment: ai-leetcode-lab, round 1
from typing import List


class Solution:
    def maxStarSum(self, vals: List[int], edges: List[List[int]], k: int) -> int:
        neighbors = [[] for _ in vals]
        for node_a, node_b in edges:
            neighbors[node_a].append(vals[node_b])
            neighbors[node_b].append(vals[node_a])

        answer = max(vals)
        for center, values in enumerate(neighbors):
            values.sort(reverse=True)
            total = vals[center]
            for value in values[:k]:
                if value <= 0:
                    break
                total += value
            answer = max(answer, total)

        return answer
