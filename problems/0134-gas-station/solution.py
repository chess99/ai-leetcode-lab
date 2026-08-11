# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-11T16:24:47Z
# Experiment: ai-leetcode-lab, round 1
from typing import List


class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        total = tank = 0
        start = 0
        for index, (available, needed) in enumerate(zip(gas, cost)):
            balance = available - needed
            total += balance
            tank += balance
            if tank < 0:
                start = index + 1
                tank = 0
        return start if total >= 0 else -1
