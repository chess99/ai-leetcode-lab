# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-11T20:21:19Z
# Experiment: ai-leetcode-lab, round 1
class Solution:
    def waysToBuyPensPencils(self, total: int, cost1: int, cost2: int) -> int:
        if cost1 < cost2:
            cost1, cost2 = cost2, cost1

        ways = 0
        for first_count in range(total // cost1 + 1):
            remaining = total - first_count * cost1
            ways += remaining // cost2 + 1

        return ways
