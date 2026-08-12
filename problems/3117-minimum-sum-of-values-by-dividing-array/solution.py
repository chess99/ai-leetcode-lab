# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-12T15:15:58Z
# Experiment: ai-leetcode-lab, round 1
from typing import List


class Solution:
    def minimumValueSum(self, nums: List[int], andValues: List[int]) -> int:
        infinity = 10 ** 18
        states = {(0, -1): 0}
        for value in nums:
            next_states = {}
            for (group, current_and), cost in states.items():
                if group == len(andValues):
                    continue
                updated_and = value if current_and == -1 else current_and & value
                target = andValues[group]
                if updated_and & target != target:
                    continue
                key = (group, updated_and)
                next_states[key] = min(next_states.get(key, infinity), cost)
                if updated_and == target:
                    key = (group + 1, -1)
                    next_states[key] = min(next_states.get(key, infinity), cost + value)
            states = next_states
        return states.get((len(andValues), -1), -1)
