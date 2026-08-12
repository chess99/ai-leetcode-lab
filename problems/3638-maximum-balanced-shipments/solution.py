# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-12T02:47:41Z
# Experiment: ai-leetcode-lab, round 1
from typing import List

class Solution:
    def maxBalancedShipments(self, weight: List[int]) -> int:
        answer = 0
        maximum = weight[0]
        for value in weight[1:]:
            if value < maximum:
                answer += 1
                maximum = -1
            else:
                maximum = max(maximum, value)
        return answer
