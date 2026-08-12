# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-12T04:46:21Z
# Experiment: ai-leetcode-lab, round 1
from typing import List


class Solution:
    def minCost(self, costs: List[List[int]]) -> int:
        red = blue = green = 0
        for cost_red, cost_blue, cost_green in costs:
            red, blue, green = (cost_red + min(blue, green),
                                cost_blue + min(red, green),
                                cost_green + min(red, blue))
        return min(red, blue, green)
