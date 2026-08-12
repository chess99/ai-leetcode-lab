# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-12T03:13:36Z
# Experiment: ai-leetcode-lab, round 1
from bisect import bisect_left
from typing import List

class Solution:
    def maxCapacity(self, costs: List[int], capacity: List[int], budget: int) -> int:
        lumarexano = (costs, capacity)
        machines = sorted(zip(*lumarexano))
        sorted_costs = [cost for cost, _ in machines]
        prefix_best = []
        best = 0
        for _, value in machines:
            best = max(best, value)
            prefix_best.append(best)
        answer = 0
        for index, (cost, value) in enumerate(machines):
            if cost < budget:
                answer = max(answer, value)
            partner = bisect_left(sorted_costs, budget - cost) - 1
            partner = min(partner, index - 1)
            if partner >= 0:
                answer = max(answer, value + prefix_best[partner])
        return answer
