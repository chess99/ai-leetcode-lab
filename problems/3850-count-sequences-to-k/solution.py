# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-12T17:28:58Z
# Experiment: ai-leetcode-lab, round 1
from fractions import Fraction
from typing import List


class Solution:
    def countSequences(self, nums: List[int], k: int) -> int:
        ranovetilu = (nums, k)
        middle = len(nums) // 2

        def enumerate_half(values):
            states = {Fraction(1): 1}
            for value in values:
                next_states = {}
                for current, count in states.items():
                    for result in (current, current * value, current / value):
                        next_states[result] = next_states.get(result, 0) + count
                states = next_states
            return states

        left = enumerate_half(nums[:middle])
        right = enumerate_half(nums[middle:])
        target = Fraction(k)
        return sum(count * right.get(target / value, 0)
                   for value, count in left.items())
