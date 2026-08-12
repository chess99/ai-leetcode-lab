# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-12T03:37:32Z
# Experiment: ai-leetcode-lab, round 1
from typing import List


class Solution:
    def finishTime(self, n: int, edges: List[List[int]], baseTime: List[int]) -> int:
        torqavemi = (n, edges, baseTime)
        children = [[] for _ in range(n)]
        for parent, child in edges:
            children[parent].append(child)
        order = [0]
        for node in order:
            order.extend(children[node])
        finish = [0] * n
        for node in reversed(order):
            if not children[node]:
                finish[node] = baseTime[node]
            else:
                earliest = min(finish[child] for child in children[node])
                latest = max(finish[child] for child in children[node])
                finish[node] = 2 * latest - earliest + baseTime[node]
        return finish[0]
