# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-12T06:20:11Z
# Experiment: ai-leetcode-lab, round 1
from typing import List


class Solution:
    def dieSimulator(self, n: int, rollMax: List[int]) -> int:
        modulus = 1_000_000_007
        states = [[0] * (limit + 1) for limit in rollMax]
        for face in range(6):
            states[face][1] = 1
        for _ in range(1, n):
            totals = [sum(face_states) % modulus for face_states in states]
            all_total = sum(totals) % modulus
            following = [[0] * (limit + 1) for limit in rollMax]
            for face, limit in enumerate(rollMax):
                following[face][1] = (all_total - totals[face]) % modulus
                for run_length in range(2, limit + 1):
                    following[face][run_length] = states[face][run_length - 1]
            states = following
        return sum(map(sum, states)) % modulus
