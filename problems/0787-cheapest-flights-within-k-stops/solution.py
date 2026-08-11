# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-11T17:43:58Z
# Experiment: ai-leetcode-lab, round 1
from typing import List


class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        costs = [float("inf")] * n
        costs[src] = 0
        for _ in range(k + 1):
            next_costs = costs[:]
            for source, target, price in flights:
                if costs[source] != float("inf"):
                    next_costs[target] = min(next_costs[target], costs[source] + price)
            costs = next_costs
        return -1 if costs[dst] == float("inf") else costs[dst]
