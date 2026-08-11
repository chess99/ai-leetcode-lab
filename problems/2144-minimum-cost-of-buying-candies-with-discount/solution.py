# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-11T13:12:00Z
# Experiment: ai-leetcode-lab, round 1
class Solution:
    def minimumCost(self, cost: List[int]) -> int:
        return sum(value for i, value in enumerate(sorted(cost, reverse=True)) if i % 3 != 2)
