# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-11T10:57:51Z
# Experiment: ai-leetcode-lab, round 1
class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        first = second = 0
        for value in cost:
            first, second = second, min(first, second) + value
        return min(first, second)
