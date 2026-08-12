# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-12T15:15:59Z
# Experiment: ai-leetcode-lab, round 1
from math import comb


class Solution:
    def waysToReachStair(self, k: int) -> int:
        answer = 0
        jumps = 0
        while (1 << jumps) - k <= jumps + 1:
            downward_steps = (1 << jumps) - k
            if downward_steps >= 0:
                answer += comb(jumps + 1, downward_steps)
            jumps += 1
        return answer
