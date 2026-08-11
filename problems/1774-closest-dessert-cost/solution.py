# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-11T19:34:28Z
# Experiment: ai-leetcode-lab, round 1
from typing import List
class Solution:
    def closestCost(self, baseCosts: List[int], toppingCosts: List[int], target: int) -> int:
        best = min(baseCosts)
        def search(index: int, cost: int) -> None:
            nonlocal best
            if abs(cost-target) < abs(best-target) or (abs(cost-target) == abs(best-target) and cost < best): best = cost
            if index == len(toppingCosts) or cost >= target: return
            search(index+1,cost); search(index+1,cost+toppingCosts[index]); search(index+1,cost+2*toppingCosts[index])
        for base in baseCosts: search(0,base)
        return best
