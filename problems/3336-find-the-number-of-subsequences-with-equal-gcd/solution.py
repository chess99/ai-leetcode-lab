# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-12T15:59:35Z
# Experiment: ai-leetcode-lab, round 1
from math import gcd
from typing import List


class Solution:
    def subsequencePairCount(self, nums: List[int]) -> int:
        modulus = 1_000_000_007
        maximum = max(nums)
        states = {(0, 0): 1}
        for value in nums:
            next_states = states.copy()
            for (first, second), ways in states.items():
                key = (gcd(first, value), second)
                next_states[key] = (next_states.get(key, 0) + ways) % modulus
                key = (first, gcd(second, value))
                next_states[key] = (next_states.get(key, 0) + ways) % modulus
            states = next_states
        return sum(ways for (first, second), ways in states.items()
                   if first == second and first > 0) % modulus
