# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-11T20:37:12Z
# Experiment: ai-leetcode-lab, round 1
from math import comb


class Solution:
    def numberOfWays(self, startPos: int, endPos: int, k: int) -> int:
        modulo = 10**9 + 7
        distance = abs(endPos - startPos)

        if distance > k or (k - distance) % 2 == 1:
            return 0

        opposite_steps = (k - distance) // 2
        return comb(k, opposite_steps) % modulo
