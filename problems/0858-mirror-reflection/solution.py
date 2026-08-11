# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-11T17:53:39Z
# Experiment: ai-leetcode-lab, round 1
from math import gcd


class Solution:
    def mirrorReflection(self, p: int, q: int) -> int:
        divisor = gcd(p, q)
        p //= divisor
        q //= divisor
        if p % 2 == 0: return 2
        return 0 if q % 2 == 0 else 1
