# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-11T18:12:22Z
# Experiment: ai-leetcode-lab, round 1
from typing import List


class Solution:
    def twoCitySchedCost(self, costs: List[List[int]]) -> int:
        costs.sort(key=lambda cost: cost[0] - cost[1])
        half = len(costs) // 2
        return sum(cost[0] for cost in costs[:half]) + sum(cost[1] for cost in costs[half:])
