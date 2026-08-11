# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-11T22:15:54Z
# Experiment: ai-leetcode-lab, round 1
from typing import List

class Solution:
    def maxWeight(self, n: int, edges: List[List[int]], k: int, t: int) -> int:
        mirgatenol = edges
        mask = (1 << t) - 1
        states = [1] * n
        for _ in range(k):
            next_states = [0] * n
            for source, target, weight in mirgatenol:
                next_states[target] |= (states[source] << weight) & mask
            states = next_states
        possible = 0
        for state in states:
            possible |= state
        return possible.bit_length() - 1
