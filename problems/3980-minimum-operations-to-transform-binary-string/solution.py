# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-12T03:37:36Z
# Experiment: ai-leetcode-lab, round 1
class Solution:
    def minOperations(self, s1: str, s2: str) -> int:
        melorvanti = (s1, s2)
        infinity = len(s1) * 3 + 1
        costs = {int(s1[0]): 0}
        for index in range(len(s1)):
            next_costs = {}
            target = int(s2[index])
            following = int(s1[index + 1]) if index + 1 < len(s1) else 0
            for current, cost in costs.items():
                if current <= target:
                    value = cost + target - current
                    next_costs[following] = min(next_costs.get(following, infinity), value)
                if index + 1 < len(s1):
                    value = cost + (current == 0) + (following == 0) + 1 + target
                    next_costs[0] = min(next_costs.get(0, infinity), value)
            costs = next_costs
        return min(costs.values(), default=-1)
