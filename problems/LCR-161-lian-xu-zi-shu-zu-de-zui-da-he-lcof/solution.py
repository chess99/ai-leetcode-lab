# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-11T15:44:51Z
# Experiment: ai-leetcode-lab, round 1
class Solution:
    def maxSales(self, sales: List[int]) -> int:
        current = best = sales[0]
        for value in sales[1:]:
            current = max(value, current + value)
            best = max(best, current)
        return best
