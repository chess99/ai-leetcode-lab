# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-12T12:52:12Z
# Experiment: ai-leetcode-lab, round 1
from typing import List


class Solution:
    def maximumANDSum(self, nums: List[int], numSlots: int) -> int:
        states = 3 ** numSlots
        negative = -10 ** 9
        dynamic = [negative] * states
        dynamic[0] = 0

        powers = [3 ** index for index in range(numSlots)]
        for value in nums:
            updated = [negative] * states
            for state, score in enumerate(dynamic):
                if score == negative:
                    continue
                for slot, place_value in enumerate(powers, 1):
                    if state // place_value % 3 < 2:
                        next_state = state + place_value
                        updated[next_state] = max(updated[next_state],
                                                  score + (value & slot))
            dynamic = updated
        return max(dynamic)
